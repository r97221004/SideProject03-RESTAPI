from flask_restful import Resource


class Home(Resource):
    def get(self):
        return {
            "名稱": "Matt's Hotel",
            "版本": "version 1",
            "關於": "個人獨立小型專案, 模擬民宿的訂房系統｡",
            "不需要註冊登入": {
                "1": "POST https://arcane-mesa-97312.herokuapp.com/users",
                "2": "GET https://arcane-mesa-97312.herokuapp.com/auth/login",
                "3": "GET https://arcane-mesa-97312.herokuapp.com/tweets",
                "4": "GET https://arcane-mesa-97312.herokuapp.com/styles",
                "5": "GET https://arcane-mesa-97312.herokuapp.com/rooms",
                "6": "GET https://arcane-mesa-97312.herokuapp.com/rooms/<stylename>",
                "7": "GET https://arcane-mesa-97312.herokuapp.com/room/<roomname>",
            },
            "需註冊登入": {
                "8": "GET https://arcane-mesa-97312.herokuapp.com/users",
                "9": "GET https://arcane-mesa-97312.herokuapp.com/user/<username>",
                "10": "GET https://arcane-mesa-97312.herokuapp.com/tweets/<username>"
            },
            "需註冊登入, 且身分認證": {
                "11": "PUT https://arcane-mesa-97312.herokuapp.com/user/<username>",
                "12": "PATCH https://arcane-mesa-97312.herokuapp.com/user/<username>",
                "13": "DELETE https://arcane-mesa-97312.herokuapp.com/user/<username>",
                "14": "POST https://arcane-mesa-97312.herokuapp.com/tweets/<username>",
                "15": "GET https://arcane-mesa-97312.herokuapp.com/reservation/<username>",
                "16": "PUT https://arcane-mesa-97312.herokuapp.com/reservation/<username>",
                "17": "DELETE https://arcane-mesa-97312.herokuapp.com/reservation/<username>"
            },
            "管理員權限": {
                "18": "POST https://arcane-mesa-97312.herokuapp.com/styles",
                "19": "POST https://arcane-mesa-97312.herokuapp.com/rooms/<stylename>",
                "20": "PATCH https://arcane-mesa-97312.herokuapp.com/room/<roomname>",
                "21": "DELETE https://arcane-mesa-97312.herokuapp.com/room/<roomname>",
            }}
