import auth

if __name__ == "__main__":
    api = auth.get_api()
    print(api.me().name)
