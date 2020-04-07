  <!DOCTYPE html>
<!-- saved from url=(0043)https://fortherecord.simonfosterdesign.com/ -->
<html class="gr__fortherecord_simonfosterdesign_com">
<head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">

<meta name="google-site-verification" content="FExEDglH6E7hrz1p-c3-Az8q6eVgHPhhPq94uy6tf4g">
<meta name="keywords" content="Simon Foster, web designer, infographics, css3, html5, record collection">
<meta name="author" content="designed and built by simon foster">
<title>Your Plot Predictor</title>


<link rel="stylesheet" href="./For The Record_files/style.css">

<!-- favicons -->
<link rel="shortcut icon" type="image/vnd.microsoft.icon" href="https://fortherecord.simonfosterdesign.com/favicon.ico">
<link rel="apple-touch-icon" href="https://fortherecord.simonfosterdesign.com/images/icon.png">


<!--[if IE]>
<script src="scripts/html5.js"></script> 
<![endif]-->
<style>
* {
  box-sizing: border-box;
}

input[type=text], select, textarea {
  width: 100%;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 4px;
  resize: vertical;

}

label {
  padding: 12px 12px 12px 0;
  display: inline-block;
}

input[type=submit] {
  background-color: #4CAF50;
  color: white;
  padding: 12px 20px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  float: right;
}

input[type=submit]:hover {
  background-color: #45a049;
}

.container {
  border-radius: 5px;
  background-color: #f2f2f2;
  padding: 20px;
}

.col-25 {
  float: left;
  width: 25%;
  margin-top: 6px;
}

.col-75 {
  float: left;
  width: 100%;
  margin-top: 6px;
}

/* Clear floats after the columns */
.row:after {
  content: "";
  display: table;
  clear: both;
}

/* Responsive layout - when the screen is less than 600px wide, make the two columns stack on top of each other instead of next to each other */
@media screen and (max-width: 600px) {
  .col-25, .col-75, input[type=submit] {
    width: 100%;
    margin-top: 0;
  }
}
</style>


</head>

<body data-gr-c-s-loaded="true">




<div id="wrapper">

<!-- header -->
<header>
<img src="images.png" style="width:300px;height:200px;">
<h1>Movie Genre <br>  <font size="5"> <div align = 'center'>By Fathi Fadlian </div> </font>  </h1>

</header>
<!-- close header -->

<!-- about text -->
<section>
    <div class="container">
        <form action="">
            <div class="row">
                <div class="col-75">
                    <input type="text" name="text" placeholder="Enter your plot" method="get" style="height:200px" />
                </div>
            </div>
            <div class="row">
                <div class="col-75">
                    <input type="submit" name="submit" />
                </div>
            </div>
        </form>
    <?php

            $text = '';
			
			if ( filter_has_var( INPUT_GET, 'submit' ) ) 
			{

				// echo '<h2>form data retrieved by using $_GET variable<h2/>';
				
				$text = $_GET['text'];
			}
			
			$curl = curl_init();

			curl_setopt_array($curl, array(
			  CURLOPT_URL => "http://127.0.0.1:5005/post_inference/",
			  CURLOPT_RETURNTRANSFER => true,
			  CURLOPT_ENCODING => "",
			  CURLOPT_MAXREDIRS => 10,
			  CURLOPT_TIMEOUT => 0,
			  CURLOPT_FOLLOWLOCATION => false,
			  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
			  CURLOPT_CUSTOMREQUEST => "POST",
			  CURLOPT_POSTFIELDS =>"{\n\t\"text\":\" $text \"}",
			  CURLOPT_HTTPHEADER => array(
			    "Content-Type: application/json"
			  ),
			));

			$response = curl_exec($curl);
			$err = curl_error($curl);

			curl_close($curl);

			if ($err) {
			  echo "cURL Error #:" . $err;
			} else {
			  //echo $response;
			  $jsonArray = json_decode($response,true);
			  $hasil = $jsonArray["hasil"];
			  echo "<h3>Hasil Analisa: <font color='red'>".$hasil."</font></h3>";
			} ?>
      <br>
<!-- <br>I have 198 records left, which are a mixture of Funk, Soul, RnB, Reggae, Jazz and Latin. I have displayed them using a variety of statistics which can be seen below.
<br>For the record: This page has no semantic value, it's just a bit of fun, done purely for my own enjoyment (and hopefully yours). Enjoy your stay.</p> -->
    </div>
  </section>


</body></html>