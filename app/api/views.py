"""
View function for api endpoints.
"""
import json
from . import api
from flask import current_app
from app.common.LinkedinController import LinkedinController
from app.common.ElasticSearchConnector import ElasticSearchConnector

es_conn = ElasticSearchConnector()
linkedinTool = LinkedinController()
linkedinPrefix = current_app.config['LINKEDIN_PREFIX']


@api.route('/add/user/<username>')
def add_use(username):
    profile = linkedinTool.extract_profile(linkedinPrefix + username)
    # add profile to elasticsearch if valid profile
    if linkedinTool.is_profile_valid():
        es_conn.add_json(profile)
    return json.dumps(profile)


@api.route('/get/users_by/<prop>/<value>')
def get_users_by(prop, value):
    # Get users from elasticsearch based on the profile property
    return es_conn.get_user_results(prop, value)


@api.route('/get/users_by/top_score')
def get_users_by_top_score():
    return es_conn.get_user_top_score_results()

