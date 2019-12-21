#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4
    hidden_discovery = dir(hidden_4)

    for i in range(len(hidden_discovery)):
        if hidden_discovery[i][0] != '_' and hidden_discovery[i][1] != '_':
            print(hidden_discovery[i])
