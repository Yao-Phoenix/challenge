<!DOCTYPE html>
<html>
  <head>
    <meta charset='utf-8'>
    <title>{% block title %}{% endblock %}</title>
    <link rel="stylesheet" href="https://cdn.bootcss.com/bootstrap/3.3.7/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
    <link rel='stylesheet' href="{{ url_for('static', filename='main.css') }}">
    <link rel='shortcut icon' href="{{ url_for('static', filename='favicon.ico') }}">
    {% block css %}{% endblock %}
  </head>
  <body>
    <nav class="navbar navbar-inverse">
      <div class="container">
        <div class="navbar-header">
          <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1" aria-expanded="false">
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="navbar-brand" href="/">Simpledu</a>
        </div>
        <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
          <ul class="nav navbar-nav">
            <li class="active"><a href="/">课程<span class="sr-only">(current)</span></a></li>
            <li><a href="{{ url_for('live.index') }}">直播</a></li>
            {% if current_user.is_authenticated and current_user.is_admin %}
              <li><a href="{{ url_for('admin.index') }}">Control</a></li>
            {% endif %}
          </ul>
          <ul class="nav navbar-nav navbar-right">       
            {% if not current_user.is_authenticated %}
              <li><a href="{{ url_for('front.register') }}">注册</a></li>
              <li><a href="{{ url_for('front.login') }}">登录</a></li>
            {% else %}
              <li class='dropdown'>
                <a href='#' class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false"><span id='username'>{{ current_user.username }}</span><span class="caret"></span></a>
                <ul class='dropdown-menu'>
                  <li><a href='#'>个人主页</a></li>
                  <li role='separator' class='divider'></li>
                  <li><a href='{{ url_for("front.logout") }}'>退出登录</a></li>
                </ul>
              </li>
            {% endif %}
          </ul>
        </div><!-- /.navbar-collapse -->
      </div><!-- /.container-fluid -->
    </nav>
    <div class='container'>
      {% with messages = get_flashed_messages(with_categories=true) %}
        {% if messages %}
          {% for category, message in messages %}
            <div class='alert alert-{{ category }}' role='alert'>
              <button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button>
              {{ message }}
            </div>
          {% endfor %}
        {% endif %}
      {% endwith %}
      {% block body %}{% endblock %}
    </div>
    <script src="{{ url_for('static', filename='main.js') }}"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
    <script src="https://cdn.bootcss.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
    {% block js %}{% endblock %}
  </body>
</html>
