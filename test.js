// class is a template for how an object is defined -- object oriented programming
class HelpTicket{
    constructor(title, body, status) {
        this.title = title
        this.body = body
        this.status = status
    }

    closeTicket() {
        this.status == "Closed"
    }


}

// const ticket = {title: "Test", "body": "This is some text", "status": "open"}

const myTicket = new HelpTicket( "Test", "This is some text", "Open")
const secondTicket = new HelpTicket("Test2", "This is some text", "Open")

myTicket.title

secondTicket.title