# Blockchain core logic
# Основна логіка блокчейну

import hashlib as _hl
import datetime as _dt
import json as _jn


class Blockchain:
    def __init__(self):
        # Initialize an empty chain / Ініціалізуємо порожній ланцюг
        self.__chain = []

        # Create the genesis block / Створюємо генезис-блок
        genesis_block = self.__create_block(
            data="genesis block",
            proof=1,
            index=1,
            previous_hash="0"
        )
        self.__chain.append(genesis_block)

    def mine_block(self, new_data: str) -> dict:
        """Mine a new block with provided data / Майнимо новий блок із переданими даними"""
        previous_block = self.get_previous_block()
        previous_proof = previous_block['proof']
        index = len(self.__chain) + 1
        proof = self.__proof_of_work(previous_proof, index, new_data)
        previous_hash = previous_block['hash']
        new_block = self.__create_block(new_data, proof, index, previous_hash)
        self.__chain.append(new_block)
        return new_block

    def get_previous_block(self) -> dict:
        """Return the latest block / Повертає останній блок у ланцюгу"""
        return self.__chain[-1]

    def __proof_of_work(self, previous_proof: int, index: int, data: str) -> int:
        """Find a valid proof of work / Пошук правильного доказу роботи"""
        new_proof = 1
        while True:
            hash_operation = _hl.sha256(
                f'{new_proof**2 - previous_proof**2 + index}{data}'.encode()
            ).hexdigest()
            if hash_operation[:4] == '0000':
                break
            new_proof += 1
        return new_proof

    def __create_block(self, data: str, proof: int, index: int, previous_hash: str) -> dict:
        """Create a new block / Створення нового блоку"""
        block = {
            'index': index,
            'timestamp': str(_dt.datetime.now()),
            'data': data,
            'proof': proof,
            'previous_hash': previous_hash
        }
        block['hash'] = self.__hash(block)
        return block

    def __hash(self, block: dict) -> str:
        """Generate SHA-256 hash of a block / Генерує SHA-256 хеш для блоку"""
        block_copy = dict(block)
        block_copy.pop('hash', None)
        encoded_block = _jn.dumps(block_copy, sort_keys=True).encode()
        return _hl.sha256(encoded_block).hexdigest()

    def get_chain(self) -> list:
        """Return full blockchain / Повертає увесь блокчейн"""
        return self.__chain

    def is_chain_valid(self) -> bool:
        """Validate blockchain integrity / Перевірка цілісності ланцюга"""
        previous_block = self.__chain[0]
        block_index = 1

        while block_index < len(self.__chain):
            current_block = self.__chain[block_index]

            # Check hash link / Перевірка хеш-посилання
            if current_block['previous_hash'] != previous_block['hash']:
                return False

            # Check proof of work / Перевірка доказу роботи
            previous_proof = previous_block['proof']
            current_proof = current_block['proof']
            index = current_block['index']
            data = current_block['data']
            hash_check = _hl.sha256(
                f'{current_proof**2 - previous_proof**2 + index}{data}'.encode()
            ).hexdigest()
            if hash_check[:4] != '0000':
                return False

            previous_block = current_block
            block_index += 1

        return True
