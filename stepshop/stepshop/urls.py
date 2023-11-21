{% load static %}

<!DOCTYPE html>
<html lang="en">

<head>

    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="">
    <meta name="author" content="">
    <link href="https://fonts.googleapis.com/css?family=Roboto:100,300,400,500,700" rel="stylesheet">

    <title>Бобёр Inc.{% block title %}{% endblock %}</title>

    <!-- Bootstrap core CSS -->
    <link href="{% static '/vendor/bootstrap/css/bootstrap.min.css' %}" rel="stylesheet">


    <!-- Additional CSS Files -->
    <link rel="stylesheet" href="{% static '/assets/css/fontawesome.css' %}">
    <link rel="stylesheet" href="{% static '/assets/css/tooplate-main.css' %}">
    <link rel="stylesheet" href="{% static '/assets/css/owl.css' %}">
    {% block css %}
    <link rel="stylesheet" href="{% static '/assets/css/flex-slider.css' %}">
    {% endblock %}
    <!--
    Tooplate 2114 Pixie
    https://www.tooplate.com/view/2114-pixie
    -->
</head>

<body>

<!-- Pre Header -->
<div id="pre-header">
    <div class="container">
        <div class="row">
            <div class="col-md-12">

                {% if user.is_authenticated %}
                <span>
                    <a href="{% url 'auth:edit' %}" class="text-light">{{ user.username }}</a>
                </span> |
                <span><a href="{% url 'auth:logout' %}" class="text-light">Выйти</a></span>
                {#<span>{{ user.last_login|date:"d/m/Y" }}</span>#}

                {% else %}
                <span><a href="{% url 'auth:login' %}" class="text-light">Войти</a></span>
                {% endif %}

            </div>
        </div>
    </div>
</div>

{% include '../inc/inc_main_menu.html' %}

{% block content %}

{% endblock %}

<!-- Sub Footer Starts Here -->
<div class="sub-footer">
    <div class="container">
        <div class="row">
            <div class="col-md-12">
                <div class="copyright-text">
                    <p>Copyright &copy; 2023&ndash;{% now "Y" %} Baber Inc.
                </div>
            </div>
        </div>
    </div>
</div>
<!-- Sub Footer Ends Here -->


<!-- Bootstrap core JavaScript -->
<script src="{% static '/vendor/jquery/jquery.min.js' %}"></script>
<script src="{% static '/vendor/bootstrap/js/bootstrap.bundle.min.js' %}"></script>


<!-- Additional Scripts -->
<script src="{% static '/assets/js/custom.js' %}"></script>
<script src="{% static '/assets/js/owl.js' %}"></script>

{% block js %}

{% endblock %}


<script language="text/Javascript">
      cleared[0] = cleared[1] = cleared[2] = 0; //set a cleared flag for each field
      function clearField(t){                   //declaring the array outside of the
      if(! cleared[t.id]){                      // function makes it static and global
          cleared[t.id] = 1;  // you could use true and false, but that's more typing
          t.value='';         // with more chance of typos
          t.style.color='#fff';
          }
      }

</script>


</body>

</html>