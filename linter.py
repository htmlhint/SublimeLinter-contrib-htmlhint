#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Mark Maday
# Copyright (c) 2015 Mark Maday
#
# License: MIT
#

"""This module exports the Htmlhint plugin class."""

import logging

import sublime
from SublimeLinter.lint import LintMatch, NodeLinter


logger = logging.getLogger("SublimeLinter.plugin.htmlhint")


class Htmlhint(NodeLinter):

    """Provides an interface to htmlhint."""

    cmd = ("htmlhint", "--format", "json", "--nocolor", "stdin")
    defaults = {"selector": "source.html"}

    def find_errors(self, output):
        """
        Override find_errors, parsing output json into json_object.

        Calls parse_message for each error found.

        """
        output_json = sublime.decode_value(output)
        logger.debug('output_json:"%s", file: "%s"', output_json, self.filename)

        for file in output_json:
            for message in file["messages"]:
                yield self.parse_message(message)

    def parse_message(self, message):
        """Parse message object into standard elements of an error and return them."""
        error_message = message["message"]
        line = message["line"] - 1
        col = message["col"]
        error_type = message["type"]

        # ignore message type of info
        if error_type == "info":
            message = None

        logger.info(
            'message -- msg:"%s", line:%s, col:%s, type: %s, message_obj:%s',
            error_message,
            line,
            col,
            error_type,
            message,
        )
        return LintMatch(
            filename=self.filename,
            line=line,
            col=col,
            error_type=error_type,
            code=message.get("rule", {}).get("id", ""),
            message=error_message,
            match=str(message),
        )
