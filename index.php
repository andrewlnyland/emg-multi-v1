<?php
session_start();
if (!isset($_SESSION['pyPID'])) {
	$_SESSION["pyPID"] = 0;
}

$pycommand = './readertest.py &'; //2>&1
$pyPIDfilename = "/tmp/EMGstatus";

if (!isset($_SESSION['init'])) {
	$_SESSION['init'] = 0;
}
$initstr = array('set', 'end');
$recording = 0;
$recordstr = 'start';
$stopped = 0;
$stopstr = array('stop', 'again');

//no !isset() as it should update each call to the server
if (!strcmp(strtoupper(substr(PHP_OS, 0, 1)), 'L')) {
	$_SESSION['temp'] = exec('/usr/bin/vcgencmd measure_temp | awk -F "[=\']" \'{print($2 * 1.8)+32}\'');
} else {
	$_SESSION['temp'] = "SNOW.0";
}
$_SESSION['temp'] .= "'F";

function initAll() {
	global $pycommand;
	global $pyPIDfilename;
	
//	$retval = system($pycommand);
//	echo $retval;		// now started by cron, not user controlled
	//while (!file_exists($pyPIDfilename));
	if (file_exists($pyPIDfilename)) {
		$_SESSION['init'] = 1;
		$_SESSION['pyPID'] = trim(file_get_contents($pyPIDfilename));
	}
}

if (isset($_POST['run'])) {
	if (!$_SESSION['init']) {
		initAll();
	} else {
//		echo "kill -INT ${_SESSION['pyPID']}";
//		$killed = system("/bin/kill -INT ${_SESSION['pyPID']}");
		if ($_SESSION['pyPID']) {
			posix_kill($_SESSION['pyPID'], 2);
		}
		$_SESSION['init'] = 0;
	}
}

if (isset($_POST['start'])) {
	posix_kill($_SESSION['pyPID'], 
			   !strcmp(strtoupper(substr(PHP_OS, 0, 1)), 'L') ? 10 : 30);
}
if (isset($_POST['stop'])) {
	posix_kill($_SESSION['pyPID'], 
			   !strcmp(strtoupper(substr(PHP_OS, 0, 1)), 'L') ? 12 : 31);
}

?>
<!doctype html>
<html>
	<head>
		<title>EMG IoT Controller</title>
		<!--<script src="script.js"></script>-->
		<link rel="stylesheet" href="styles.css" type="text/css">
		<meta name="viewport" content="width=device-width, initial-scale=1">
	</head>
	<body>
		<?php include 'header.php'; ?>
		<section id="controls">
			<form action="" name="run" method="post">
				<button type="submit" name="run">
					<?php echo $initstr[$_SESSION['init']]; ?>
				</button>
			</form>
			<form action="" name="start" method="post">
				<button type="submit" name="start">Start</button>
			</form>
			<form action="" name="stop" method="post">
				<button type="submit" name="stop">Stop</button>
			</form>
		</section>
	</body>
</html>
