import java.io.*;
import java.net.*;

public class pingVideoConnect
{
	public static void main(String[] args)
	{
		DatagramSocket udpsoc;
		Process p;
		byte[] buf = new byte[1];
		DatagramPacket packet = new DatagramPacket(buf,buf.length);
		try
		{
			udpsoc = new DatagramSocket(5000);
			System.out.println("Waiting for reception");
			udpsoc.receive(packet);
			System.out.println("Hey! I got one!");
			InetAddress inet_ip = packet.getAddress();
			String ip_laptop = inet_ip.toString();
			ip_laptop = ip_laptop.substring(1,ip_laptop.length());

			BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(new FileOutputStream("ip_laptop.txt"), "utf-8"));
			writer.write(""+ip_laptop);
			writer.flush();
			System.out.println(ip_laptop);
			//String toExecute = "raspivid -t 999999 --hflip -o - -w 512 -fps 15 | nc "+ip_laptop+" 5000"; 
			String toExecute = "bash startCameraStream.sh"; 
			p = Runtime.getRuntime().exec(toExecute);
			System.out.println("to execute "+toExecute);
			p.waitFor();
			System.out.println("Done!");
		}
		catch(Exception e)
		{
			System.out.println("Something got fudgy!");
		}
	}

}
