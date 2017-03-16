<?php
//    最基本的链接数据库
    $servername = 'localhost';
    $username = 'root';
    $password = '9981aa';
    $tablename = 'justTest';

    $conn = new mysqli($servername,$username,$password,$tablename);
    if ($conn -> connect_error) {
        die("连接失败：" . $conn->connect_error);
    }
    // echo "连接成功";

//    $sql = "SELECT * FROM lagou WHERE location='shenzhen' AND job = 'iOS'";

   // $sql = "SELECT * FROM lagou WHERE location='shenzhen'";
    $sql = "SELECT * FROM lagou inner join zhaopingou on lagou.la_md5=zhaopingou.zhao_md5 WHERE lagou.lg_job='iOS'";

    $result = $conn->query($sql);

    if ($result->num_rows >0) {
        while ($row = $result->fetch_assoc()) {
            foreach($row as $key=>$value)
            {
                echo $key."=>".$value;
            }
        }
    } else {
        echo "0 个结果";
    }

    $conn->close();



