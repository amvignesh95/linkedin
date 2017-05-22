<%-- 
    Document   : authentication
    Created on : Apr 9, 2017, 12:03:06 PM
    Author     : vino
--%>

<%@page contentType="text/html" pageEncoding="UTF-8"%>
<%@page import="java.sql.SQLException"%>
<%@page import="java.sql.ResultSet" %>
<%@page import="java.sql.PreparedStatement" %>
<%@page import="java.sql.DriverManager" %>
<%@page import="java.sql.Connection" %>

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
   "http://www.w3.org/TR/html4/loose.dtd">

<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>JSP Page</title>
    </head>
    <body>
        <%
            String id = request.getParameter("v1");
            String fin = request.getParameter("v2");
            out.println(id);
            out.println(fin);
        %>
        <%
            try{
                Class.forName("com.mysql.jdbc.Driver");
                Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/jobs?zeroDateTimeBehavior=convertToNull","root","");
                PreparedStatement ps = con.prepareStatement("select * from login where username=? and password=?");
                ps.setString(1,id);
                ps.setString(2,fin);
                ResultSet rs=ps.executeQuery();
                if(rs.next())
                    {
                    response.sendRedirect("positive.html");
                }
                else
                    {
                    response.sendRedirect("negative.html");
                    }
                }
            catch(Exception e)
                    {
                }
        %>
    </body>
</html>
