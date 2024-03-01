package main

import (
	"fmt"
	"net/smtp"
)

func main() {
	// SMTP 서버 정보 설정
	host := "smtp.gmail.com"
	port := "587"

	// 보내는 사람 정보
	from := "@email"       // email
	password := "password" // ex) Google 2-factor password

	// 받는 사람 정보
	toList := []string{""} // receiver email

	// 이메일 내용
	msg := "Hello, this is a test email from Go!"

	// SMTP 인증 설정
	auth := smtp.PlainAuth("", from, password, host)

	// 이메일 보내기a
	err := smtp.SendMail(host+":"+port, auth, from, toList, []byte(msg))
	if err != nil {
		fmt.Println("이메일 전송 실패:", err)
		return
	}

	fmt.Println("이메일이 성공적으로 전송되었습니다!")

}
