Imports System.Data
Imports System.Data.OleDb
Imports System.Data.OleDb.OleDbConnection
Imports System.Data.OleDb.OleDbCommand

Public class form1

Private Sub Button1_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button1.Click
        Dim count As Integer = 0
        Dim count1 As Integer = 0
        Dim count2 As Integer = 0
        Dim count3 As Integer = 0
        Dim query As String = "select * from association"
        Dim conection As String = "Provider=MSDAORA;Data Source=XE;Persist Security Info=True;User ID=system;Password=system;Unicode=True"
        Dim con As New OleDbConnection(conection)
        Dim cmd As New OleDbCommand(query, con)
        con.Open()
        Dim dr As OleDbDataReader = cmd.ExecuteReader()
        While (dr.Read())
            Dim m As String
            m = dr.GetString(1).ToString()
            If (m.Contains(TextBox1.Text) = True) Then
                If (m.Contains(TextBox2.Text) = True) Then
                    count1 = count1 + 1  '(AUB)
                End If
                count2 = count2 + 1    '(A)
            End If
            count = count + 1     'n
            If (m.Contains(TextBox2.Text) = True) Then
                count3 = count3 + 1   '(B)
            End If
        End While
        If (count = 0) Then
            MessageBox.Show("No record found")
        Else
            TextBox3.Text = count
            TextBox4.Text = (count2 / count) * 100
            TextBox5.Text = (count3 / count) * 100
            TextBox6.Text = (count1 / count) * 100
            TextBox7.Text = (count1 / count2) * 100    

        End If
    End Sub
End Class
