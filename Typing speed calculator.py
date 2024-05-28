import time

def main():
    # Set the sentence for typing
    sentence = "The quick brown fox jumps over the lazy dog."

    # Prompt the user to start typing
    input("Type the following sentence and press Enter:\n\n{}\n\n".format(sentence))

    # Record the start time
    start_time = time.time()

    # Prompt the user to retype the sentence
    typed_sentence = input("Retype the sentence: ")

    # Record the end time
    end_time = time.time()

    # Calculate the time taken in seconds
    elapsed_time = end_time - start_time

    # Calculate the number of words in the sentence
    word_count = len(sentence.split())

    # Calculate the typing speed in words per minute (WPM)
    wpm = (word_count / elapsed_time) * 60

    # Calculate accuracy
    accuracy = calculate_accuracy(sentence, typed_sentence)

    # Provide feedback
    print("\nTyping speed: {:.2f} WPM".format(wpm))
    print("Accuracy: {:.2f}%".format(accuracy * 100))

def calculate_accuracy(original, typed):
    correct_chars = sum(c1 == c2 for c1, c2 in zip(original, typed))
    total_chars = len(original)
    return correct_chars / total_chars

if __name__ == "__main__":
    main()
