# Beautiful is better than ugly ==")
print("\n=== 1. Beautiful is better than ugly ===")
# Ugly
x=[i for i in range(10) if i%2==0]
# Beautiful
even_numbers = [i for i in range(10) if i % 2 == 0]

# 2.Explicit is better than implicit.
print("\n=== 2. Explicit is better than implicit ===")
# Implicit
def process(data):
    return data.strip().lower().split()
# Explicit
def process_text(text: str) -> list[str] :
    """Process text by stripping, lowercasing, and splitting. """
    cleaned = text.strip()
    lowered = cleaned.lower()
    words = lowered.split()
    return words
#3. Simple is better than complex ===")
# Complex
def is_prime_complex(n):
    if n<=1:
        return False
    if n<=3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <=n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
        return True
    #Simple
    def is_prime_simple(n: int) -> bool:
        """Check if a number is prime."""
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) +1):
            if n % i == 0:
                return False
            return True
        print(f"Prime check 17: {is_prime_simple(17)}")

        # 4. Complex is better than complicated.
        print("\n==4. Complex is better than complicated ===")
        class DatabaseConnection:
            """Complex but not complicated - proper abstraction"""
            def __init__(self, config):
                self.config = config
                self._connection = None

                def connect(self):
                    pass
                def execute(self, query):
                    pass
                # 5. Flat is better than nested
                print("\n=== 5. Flat is better than nested ===")
                #Nested (bad)
                def process_data_nested(data):
                    if data:
                        if isiinstance(data, list):
                            if len(data) > 0:
                                for item in data:
                                    if item:
                                        return item.upper()
                                    return None
                                def process_data_flat(data):
                                    if not data:
                                        return None
                                    if not isinstance(data, list):
                                        return None
                                    for item in data:
                                        if item:
                                            return item.upper()
                                        return None            
