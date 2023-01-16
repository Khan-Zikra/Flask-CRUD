from flask_restful import Resource
import logging as logger

class Task(Resource):   # The Task class inheritng from Resourcethe  class


    def get(self):
        logger.debug("Inside get methode ")
        return{"message": "Inside get method"},200

    def post(self):
        logger.debug("Inside post methode ")
        return{"message": "Inside post method"},200


    def put(self):
       logger.debug("Inside put methode ")
       return{"message": "Inside put method"},200


    def delete(self):
        logger.debug("Inside delete methode ")
        return{"message": "Inside delete method"},200

 