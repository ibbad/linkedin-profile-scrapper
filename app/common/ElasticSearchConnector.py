"""
Elastic search connector module to handle communications with Elasticsearch
for adding and adding profiles.
"""

import json
from elasticsearch import Elasticsearch


class ElasticSearchConnector(Elasticsearch):
    els = Elasticsearch()

    els_index = 'profile'
    els_type = 'user'

    def add_json(self, json_element):
        self.els.create(self.els_index, self.els_type, json_element)

    def get_user_results(self, key, value):
        results = self.els.search(self.els_index, self.els_type,
                                  body={
                                      "query": {
                                          "match": {
                                              key: value
                                          }
                                      }
                                  })
        return self.get_elastic_results(results)

    def get_user_top_score_results(self):
        results = self.els.search(self.els_index, self.els_type, body={
            "query": {
                "function_score": {
                    "functions": [
                        {
                            "field_value_factor": {
                                "field": "RECOMMENDATIONS_NUMBER",
                                "factor": 1.5
                            }
                        }
                    ],
                    "query": {
                        "match": {
                            "EDUCATION.NAME": "degree university college "
                                              "academy"
                        }
                    },
                    "score_mode": "avg"
                }
            }
        })
        return self.get_elastic_results(results)

    def get_elastic_results(self, results):
        # Add number of results from Elastic's JSON response
        response = '[{"Number.of.results": %num'.format(
            num=results['hits']['total'])

        # print all results concatenated together
        for result in results['hits']['hits']:
            response += '%s' % json.dumps(result['_source'])

        return response + '{}]'
