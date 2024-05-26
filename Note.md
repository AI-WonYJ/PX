Public Function CountPd() As Integer
	CountPd = Application.WorkSheetFunction.Count(Range("D1:D16"))
End Function

Public Function SumPrice() As Long
	Dim Sum As Long
	Sum = 0
	For i = 1 To CountPd()+1
		Sum = Sum + Cells(i, 5)
	Next i
	SumPrice = Sum
End Function

Sub Cal_Each_Price()
	Dim i As Integer
	Dim CountPdt As Integer
	CountPdt = CountPd()
	Range("C17") = CountPdt
	Range("E2").Select
	Range("E2:E16").Clear
	For i = 0 To CountPdt-1
		ActiveCell.Offset(i, 0) = Cells(i+2, 2)*Cells(i+2, 3)*Cells(i+2, 4)
		ActiveCell.Offset(i, 0).Font.Color = vbBlue
	Next i
	Range("C18") = SumPrice()
End Sub

Sub Budget_Cal()
	Dim i As Integer
	Dim Budget As Long
	Dim CountPdt As Integer
	Dim j As Integer
	Dim k As Integer
	k = 27
	CountPdt = CountPd()
	Budget = Range("C19")
	Do While 1
		i = CountPdt-1
		If SumPrice() = Budget Then
			For j = 1 To CountPdt
				Cells(k, j+1) = Cells(j+1, 4)
			Next j
			k = k+1
			Cells(k, 1) = 100
			Do While 1 >= 0 And SumPrice() >= Budget
				Cells(i+1, 4) = 1
				i = i -1
			Loop
			If i < 0 Then
				MsgBox "Exit 1"
				Exit Do
			End If
			Cells(i, 4) = Cells(i+1, 4) + 1
		End If
	Loop
End Sub
