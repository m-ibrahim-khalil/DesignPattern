class IObserver:
    def getNotification(self):
        pass


class SmsObserver(IObserver):
    def getNotification(self):
        print("Notify by SMS")


class EmailObserver(IObserver):
    def getNotification(self):
        print("Notify by email")


class AccountObserver(IObserver):
    def getNotification(self):
        print("Notify while active")


class YoutubeChanel:
    iObserver = []

    def subscribe(self, observer):
        self.iObserver.append(observer)

    def unsubscribe(self,observer):
        self.iObserver.remove(observer)

    def notify(self):
        for i in self.iObserver:
            i.getNotification()

    def videoUpload(self):
        self.notify()


if __name__ == '__main__':
    smsObserver = SmsObserver()
    youtubeChanel = YoutubeChanel()
    youtubeChanel.subscribe(smsObserver)
    youtubeChanel.unsubscribe(smsObserver)
    youtubeChanel.subscribe(EmailObserver())
    youtubeChanel.subscribe(AccountObserver())
    youtubeChanel.videoUpload()