import sys


class HousingException(Exception):
    def __init__(self, error_message: Exception, err_detail: sys):
        super().__init__(error_message)
        self.error_message = HousingException.get_detailed_error_msg(error_message, err_detail)

    @staticmethod
    def get_detailed_error_msg(error_message, err_detail) -> str:
        """
        This function will return detailed error message for a particular exception.
        :param error_message: Exception object
        :param err_detail: object of sys module
        :return: error message
        """
        _, _, exec_tb = err_detail.exc_info()

        line_num = exec_tb.tb_frame.f_lineno
        file_name = exec_tb.tb_frame.f_code.co_filename

        error_message = f"Error occurred in script: {file_name} at line number: {line_num} error msg: {error_message}"
        return error_message

    def __str__(self):
        return self.error_message

    def __repr__(self) -> str:
        return HousingException.__name__.str()
