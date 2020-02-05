from flask import Blueprint, Response, jsonify
from flask import render_template
from analysis import job as job_

job = Blueprint('job', __name__, url_prefix='/job')

@job.route('/')
def index():
    return render_template('job/index.html')

@job.route('/count_top10')
def count_top10():
    return render_template('job/count_top10.html', query=job_.count_top10())

@job.route('/salary_top10')
def salary_top10():
    return render_template('job/salary_top10.html', query=job_.salary_top10())

@job.route('/hot_tags')
def hot_tags():
    query = job_.hot_tags().to_dict('reconds')
    return render_template('job/hot_tags.html', query=query)

@job.route('/hot_tags.png')
def hot_tags_plot():
    return Response(job_.hot_tags_plot(), content_type='image/png')

@job.route('/experience')
def experience():
    return render_template('job/experience.html', query=job_.experience())

@job.route('/experience.json')
def experience_json():
    return jsonify(job_.experience())

@job.route('/education')
def education():
    return render_template('job/education.html', query=job_.education())

@job.route('/education.json')
def education_json():
    return jsonify(job_.education())

@job.route('/same_education_different_cities_salary')
def same_education_different_cities_salary():
    return render_template(
            'job/same_education_different_cities_salary.html',
            query=job_.same_education_different_cities_salary())
@job.route('/same_education_different_cities_salary.json')
def same_education_different_cities_salary_json():
    return jsonify(job_.same_education_different_cities_salary())
