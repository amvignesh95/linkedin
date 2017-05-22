import java.awt.*;
import java.awt.event.*;
import java.sql.*;
import javax.swing.*;
public class OnlinePurchase extends Frame implements ActionListener
{
	String role="";
	Frame f1,f2,f3,f4;
	TextField tname,taddress,tcontact,temail,tpassword,tid,tpass;
	PreparedStatement pst1=null,pst2=null;
	Connection con=null;
	ResultSet rs=null;
	Statement st=null;

	public  OnlinePurchase()
	{
	 f1 = new Frame("Online Shopping");
	f1.setSize(500,300);
	f1.setBackground(Color.pink);
	f1.setVisible(true);
	f1.setLocationRelativeTo(null);
	f1.setLayout(new FlowLayout());
	
	f1.addWindowListener(new WindowAdapter()
	{
		public void windowClosing(WindowEvent e)
		{
			System.exit(0);
		}
	});
	Button company=new Button("Company");
	Button customer=new Button("Customer");
	company.addActionListener(this);
	customer.addActionListener(this);
	f1.add(company);
	f1.add(customer);	
	}
	

	public void actionPerformed(ActionEvent e)
	{
		Button b=(Button)e.getSource();
		if(b.getLabel().equals("Company") || b.getLabel().equals("Customer"))
			makeFrame(b.getLabel());
		else if(b.getLabel().equals("Company Login") || b.getLabel().equals("Customer Login"))
			slogin(b.getLabel());
		else if(b.getLabel().equals("Company Signup") || b.getLabel().equals("Customer Signup"))
			ssignup(b.getLabel());
		else if(b.getLabel().equals("Signup"))
			signupuser();
		else if(b.getLabel().equals("Login"))
			loginuser();
		else if(b.getLabel().equals("Reset"))
			reset();
	}
	public void makeFrame(String str)
	{
		role=str;
		f2=new Frame();
		f1.setVisible(false);
		f2.setLayout(new FlowLayout());
		f2.setBackground(Color.pink);
		f2.setSize(500,300);
		f2.setVisible(true);
		f2.setLocationRelativeTo(null);
		f2.setResizable(false);
		f2.addWindowListener(new WindowAdapter()
		{
			public void windowClosing(WindowEvent e)
			{
				f1.setVisible(true);
			}
		});
		Button login=new Button(str+" Login");
		Button signup=new Button(str+" Signup");
		login.addActionListener(this);
		signup.addActionListener(this);
		f2.add(login);
		f2.add(signup);
	}

	public void slogin(String str)
	{
		f3=new Frame();
		f2.setVisible(false);	
		f3.setBackground(Color.pink);
		f3.setLayout(new GridBagLayout());
		f3.setSize(500,300);		
		f3.setVisible(true);
		f3.setLocationRelativeTo(null);
		f3.setResizable(false);
	
		GridBagConstraints gbc=new GridBagConstraints();
		Label head=new Label(str);
		gbc.weightx=1;
		gbc.gridheight=2;
		gbc.gridwidth=2;
		Font f=new Font("Times new roman",Font.PLAIN,23);
		head.setFont(f);                                  
		f3.add(head,gbc);
		gbc.gridheight=1;
		gbc.gridwidth=1;
		gbc.gridx=0;
		gbc.gridy=2;
		f3.setBackground(Color.blue);
		
		Label lid=new Label("User ID");
		f3.add(lid,gbc);
		tid=new TextField();
		gbc.ipadx=60;
		gbc.gridx=1;
		gbc.gridy=2;
		f3.add(tid,gbc);
		
		Label lpassword=new Label("Password");
		gbc.ipadx=0;
		gbc.gridx=0;
		gbc.gridy=3;
		f3.add(lpassword,gbc);	
		tpassword=new TextField();
		gbc.ipadx=60;
		gbc.gridx=1;
		gbc.gridy=3;
		f3.add(tpassword,gbc);
		
		Button sign=new Button("Login");
		gbc.gridwidth=2;
		gbc.gridx=0;
		gbc.gridy=4;
		f3.add(sign,gbc);
		gbc.gridwidth=2;
		gbc.gridx=0;
		gbc.gridy=5;
		
		Button reset=new Button("Reset");
		f3.add(reset,gbc);
		f3.setResizable(false);
		f3.setVisible(true);
		sign.addActionListener(this);
		reset.addActionListener(this);
	
		f3.addWindowListener(new WindowAdapter()
		{
		public void windowClosing(WindowEvent we)
		{
			f2.setVisible(true);
		}
		});
		}
	
	public void ssignup(String str)
	{
		f4=new Frame();
		f2.setVisible(false);
		f4.setLayout(new FlowLayout());
		f4.setBackground(Color.pink);
		f4.setSize(500,300);		
		f4.setVisible(true);
		f4.setLocationRelativeTo(null);
		
		Label head=new Label(str);
		Font f=new Font("Time new roman",Font.PLAIN,24);
		head.setFont(f);
		head.setBackground(Color.green);
		f4.add(head);
		Panel panel=new Panel();
		panel.setLayout(new GridLayout(6,2,10,10));
		panel.setBackground(Color.magenta);
	
		Label name=new Label("Name : ");
		tname=new TextField();
	
		Label address=new Label("Address : ");
		taddress=new TextField();
	
		Label contact=new Label("Contact No : ");
		tcontact=new TextField();
	
		Label email=new Label("Email : ");
		temail=new TextField();
		
		Label password=new Label("Password: ");
		tpass=new TextField();
		
		Button signup=new Button("Signup");
		Button reset=new Button("Reset");
		signup.addActionListener(this);
		reset.addActionListener(this);
	
		panel.add(name);
		panel.add(tname);
		panel.add(address);
		panel.add(taddress);
		panel.add(contact);
		panel.add(tcontact);		
		panel.add(email);
		panel.add(temail);
		panel.add(password);
		panel.add(tpass);
		panel.add(signup);
		panel.add(reset);
		f4.add(panel);
		f4.addWindowListener(new WindowAdapter()
		{
		public void windowClosing(WindowEvent we)
		{
		f2.setVisible(true);
		}
		});			
	}
	public void reset()
	{   
		tname.setText("");
		taddress.setText("");
		tcontact.setText("");
		temail.setText("");
		tpassword.setText("");
		tid.setText("");
		tpass.setText("");
	}
	public void signupuser()
	{
		String name=tname.getText();
		String address=taddress.getText();
		String email=temail.getText();
		int contact=Integer.valueOf(tcontact.getText());
		String pass = tpass.getText();
		try
		{
		Class.forName("oracle.jdbc.driver.OracleDriver");
		con=DriverManager.getConnection("jdbc:oracle:thin:@localhost:1521:xe","system","system");
		if(role.equals("Company"))
		{
		pst1=con.prepareStatement("insert into company values(?,?,?,?,?)");
		pst2=con.prepareStatement("insert into companylogin values(?,?)");
		}
		else if(role.equals("Customer"))
		{
		pst1=con.prepareStatement("insert into customer values(?,?,?,?,?)");
		pst2=con.prepareStatement("insert into customerlogin values(?,?)");		
		}
		pst1.setString(1,name);
		pst1.setString(2,address);
		pst1.setInt(3,contact);
		pst1.setString(4,email);
		pst1.setString(5,pass);
		pst2.setString(1,email);
		pst2.setString(2,pass);
		int i=pst1.executeUpdate();
		int j=pst2.executeUpdate();
		if(i!=0 && j!=0)	
		{
		JOptionPane.showMessageDialog(null,"Updated Successfully");
		}
		else
		JOptionPane.showMessageDialog(null,"Not updated");
		f2.setVisible(true);
		}
		catch(Exception e)
		{
			JOptionPane.showMessageDialog(null,e.getMessage());
		}
	}
	
	public void loginuser()
	{
		String mail_id=tid.getText();
		String pass=tpassword.getText();
		int k=0;
		try{
		Class.forName("oracle.jdbc.driver.OracleDriver");
		con=DriverManager.getConnection("jdbc:oracle:thin:@localhost:1521:xe","system","system");
		st=con.createStatement();
		if(role.equals("Company"))
		rs=st.executeQuery("select * from companylogin");
		else 
		rs=st.executeQuery("select * from customerlogin");
		while(rs.next())
		{
			if(rs.getString(1).equals(mail_id) && rs.getString(2).equals(pass))
			{
				JOptionPane.showMessageDialog(null,"Valid Credential");
				k=1;
				/*if(role.equals("Company"))
					JOptionPane.showMessageDialog(null,"Company Login Successfully");
				else if(role.equals("Customer"))
					JOptionPane.showMessageDialog(null,"Customer Login Successfully");*/
			}
		}
		if(k!=1)
				JOptionPane.showMessageDialog(null,"Invalid Credential");
		}
		catch(Exception e)
		{
				JOptionPane.showMessageDialog(null,e.getMessage());
			
		}
	}
	public static void main(String[] args)
	{
		OnlinePurchase op = new OnlinePurchase();
	}
	
}