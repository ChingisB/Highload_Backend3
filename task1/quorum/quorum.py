import requests

class QuorumTester:

    def perform_test(self, hosts: list[str]) -> bool:
        pass



class ReadQuorumTester(QuorumTester):
    R = 2


    def perform_test(self, hosts: list[str]) -> bool:
        responses = []
        for host in hosts:
            try:
                response = requests.get(url=f"{host}/api/name/")
                if response.status_code == 200:
                    responses.append(response.json()["value"])
            except:
                continue
        return max(responses, key=responses.count) >= self.R


class WriteQuorumTester(QuorumTester):
    W = 2

    def perform_test(self, hosts: list[str]) -> bool:
        responses_count = 0
        for host in hosts:
            try:
                response = requests.put(url=f"{host}/api/name", data={"value": "new_value"})
                if response.status_code == 200:
                    responses_count += 1
            except:
                continue
        return responses_count >= self.W


if __name__ == "__main__":
    HOSTS = ["https://localhost:8000", "https://localhost:8001", "https://localhost:8002"]
    read_tester = ReadQuorumTester()
    write_tester = WriteQuorumTester()

    if read_tester.perform_test(HOSTS):
        print("READ QUORUM REACHED")
    else:
        print("NO READ QUORUM")
    

    if write_tester.perform_test(HOSTS):
        print("WRITE QUORUM REACHED")
    else:
        print("NO WRITE QUORUM")

