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

import sublime
from SublimeLinter.lint import NodeLinter, persist


class Htmlhint(NodeLinter):

    """Provides an interface to htmlhint."""

    cmd = ('htmlhint', '--format', 'json', '--nocolor', 'stdin')
    defaults = {
        'selector': 'text.html'
    }

    def find_errors(self, output):
        """
        Override find_errors, parsing output json into json_object.

        Calls parse_message for each error found.

        """
        output_json = sublime.decode_value(output)

        # persist.debug('output_json:"{}", file: "{}"'.format(output_json, self.filename))

        for file in output_json:
            for message in file['messages']:
                yield self.parse_message(message)

    def parse_message(self, message):
        """Parse message object into standard elements of an error and return them."""
        error_message = message['message']
        line = message['line'] - 1
        col = message['col']

        # set error and warning flags based on message type
        error = None
        warning = None
        if message['type'] == 'error':
            error = True
            warning = False
        elif message['type'] == 'warning':
            error = False
            warning = True
        elif message['type'] == 'info':
            # ignore info messages by setting message to None
            message = None

        message = 'message -- msg:"{}", line:{}, col:{}, error: {}, warning: {}, message_obj:{}'
        persist.debug(message.format(
            error_message,
            line,
            col,
            error,
            warning,
            message,
        ))

        return message, line, col, error, warning, error_message, None
