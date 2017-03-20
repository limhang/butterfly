<?php
//    最基本的链接数据库
//    $servername = 'localhost';
//    $username = 'root';
//    $password = '9981aa';
//    $tablename = 'justTest';
    require_once ('dbconnect.php');
    $conn = new mysqli($servername,$username,$password,$tablename);
    if ($conn -> connect_error) {
        die("连接失败：" . $conn->connect_error);
    }
    $sql_time = date("Y-m-d",strtotime("-1 day"));
    $sql = "SELECT * FROM lagou inner join zhaopingou on lagou.la_md5=zhaopingou.zhao_md5 WHERE lagou.lg_job='Android' AND lagou.lg_time='$sql_time'";
    $result = $conn->query($sql);

    if ($result->num_rows >0) {
        $data_analysis = array();
        while ($row = $result->fetch_assoc()) {
            array_push($data_analysis,$row);
        }
        echo json_encode($data_analysis);
    } else {
        echo "0 个结果";
    }
    $conn->close();



