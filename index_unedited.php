<html>
	<body>
		<form action="">
			<!-- <input type="file" method="post" enctype="multipart/form-data"/> -->
			Text : <input type="text" name="text" placeholder="text dong" method="get" />
			<input type="submit" name="submit" />
		</form>
		<?php
			
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
			  echo "<h1>Hasil Analisa: <font color='red'>".$hasil."</font></h1>";
			} ?>
	</body>
</html>