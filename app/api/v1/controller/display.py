from app.api.v1.utils.error_file import en_errors
from flask import jsonify

class Display():

    def render(self,status):
        if not isinstance(self.data,dict) or isinstance(self.data,list):
            return jsonify(
                {
                    "status":500,
                    "error":"invalid data passed to display method"
                }
            ),status
        else:
            return jsonify(
                {
                    "status": status,
                    "data": self.data
                }
            ),status

    @staticmethod
    def error_display(error:int,status:int):
        return jsonify(
            {
                "error":en_errors[error],
                "status":status
            }
        ),status


    @staticmethod
    def custom_render(data,status):
        return jsonify(
            {
                "status": status,
                "data": data
            }
        ),status

    @staticmethod
    def display_error(code,status):
        return jsonify(
            {
                "status":status,
                "error":en_errors[code]
            }
        )

    def render_internal_error(self):
        try:
            n= self.data_error
            return jsonify({
                "error":en_errors[n],
                "status":400
            })
        except:
            return jsonify(
                {
                    "status":201,
                    "data":self.data
                }
            ),201