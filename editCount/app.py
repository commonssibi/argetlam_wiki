#!/usr/bin/python
from flask import Flask, jsonify
from flask import abort
from flask import make_response
from utility import articleEditInfo,getArticleEditCount
app = Flask(__name__)


''' To get the total number of edits across the edit a thon '''
@app.route('/editCount/api/v1.0/total', methods = ['GET'])
def get_total_count():
    return jsonify( { 'data': data } )

''' To get the edit count of each article '''
@app.route('/editCount/api/v1.0/article/<name>', methods = ['GET'])
def get_article_count(name):
    if name in articleEditInfo:
        return jsonify( { 'count': articleEditInfo[name] } )
    else:
        abort(404)

''' To get all article related info & edit count '''
@app.route('/editCount/api/v1.0/article/', methods = ['GET'])
def get_article_count_all():
    getArticleEditCount()
    return jsonify( { 'data': articleEditInfo } )

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify( { 'error': 'Not found' } ), 404)

if __name__ == '__main__':
    app.run(debug = True)