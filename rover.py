
##version 5

# def move(plateau, rover_position, instructions):
#     directions = ["N", "E", "S", "W"]
#     x, y, direction = rover_position

#     for instruction in instructions:
#         if instruction == "L":
#             direction = directions[(directions.index(direction) - 1 + 4) % 4]
#         elif instruction == "R":
#             direction = directions[(directions.index(direction) + 1) % 4]
#         elif instruction == "M":
#             next_x, next_y = x, y

#             if direction == "N":
#                 next_y += 1
#             elif direction == "E":
#                 next_x += 1
#             elif direction == "S":
#                 next_y -= 1
#             elif direction == "W":
#                 next_x -= 1

#             # Check if the next position is out of bounds
#             if next_x < 0 or next_x > plateau[0] or next_y < 0 or next_y > plateau[1]:
#                 raise ValueError(f"Rover moved out of plateau bounds: ({next_x}, {next_y}).")

#             x, y = next_x, next_y
#         else:
#             raise ValueError("Invalid instruction detected.")

#     return x, y, direction


# def process_rovers():
#     try:
#         plateau = tuple(map(int, input("Enter plateau dimensions (e.g., '5 5'): ").split()))
#         if len(plateau) != 2 or any(n < 0 for n in plateau):
#             print("Invalid input format for plateau dimensions.")
#             return
#     except ValueError:
#         print("Invalid input format for plateau dimensions.")
#         return

#     results = []

#     while True:
#         position_input = input("Enter rover position (e.g., '1 2 N') or 'STOP' to finish: ")
#         if position_input.strip().upper() == "STOP":
#             break

#         try:
#             position = position_input.split()
#             if len(position) != 3 or not position[0].isdigit() or not position[1].isdigit() or position[2] not in ["N", "E", "S", "W"]:
#                 print("Invalid rover position format. Please try again.")
#                 continue

#             x, y = int(position[0]), int(position[1])
#             if x < 0 or x > plateau[0] or y < 0 or y > plateau[1]:
#                 print(f"Invalid rover position: ({x}, {y}) is outside plateau bounds. Please try again.")
#                 continue

#             direction = position[2]

#             instructions = input("Enter instructions for the rover (e.g., 'LMLMLMLMM'): ").strip()
#             if not instructions.isalpha() or not set(instructions).issubset({"L", "R", "M"}):
#                 print("Invalid instructions format.")
#                 results.append(f"{x} {y} {direction} - Failed: Invalid instructions")
#                 continue

#             try:
#                 final_position = move(plateau, (x, y, direction), instructions)
#                 results.append(f"{final_position[0]} {final_position[1]} {final_position[2]}")
#             except ValueError as e:
#                 results.append(f"{x} {y} {direction} - Failed: {str(e)}")

#         except Exception as e:
#             print(f"An error occurred: {str(e)}. Please try again.")
#             continue

#     if results:
#         print("\nResults:")
#         for i, result in enumerate(results, 1):
#             print(f"Rover {i}: {result}")


# if __name__ == "__main__":
#     process_rovers()








## version 6

# def move(plateau, rover_position, instructions):
#     directions = ["N", "E", "S", "W"]
#     x, y, direction = rover_position

#     for instruction in instructions:
#         if instruction == "L":
#             direction = directions[(directions.index(direction) - 1 + 4) % 4]
#         elif instruction == "R":
#             direction = directions[(directions.index(direction) + 1) % 4]
#         elif instruction == "M":
#             next_x, next_y = x, y

#             if direction == "N":
#                 next_y += 1
#             elif direction == "E":
#                 next_x += 1
#             elif direction == "S":
#                 next_y -= 1
#             elif direction == "W":
#                 next_x -= 1

#             if next_x < 0 or next_x > plateau[0] or next_y < 0 or next_y > plateau[1]:
#                 raise ValueError(f"Rover moved out of plateau bounds: ({next_x}, {next_y})")

#             x, y = next_x, next_y

#     return x, y, direction

# def process_rovers():
#     try:
#         plateau = tuple(map(int, input().split()))
#         if len(plateau) != 2 or any(n < 0 for n in plateau):
#             raise ValueError("Invalid plateau dimensions")
#     except ValueError as e:
#         print(str(e))
#         return

#     while True:
#         try:
#             position_input = input()
#             if not position_input:
#                 break

#             position = position_input.split()
#             if len(position) != 3 or not position[0].isdigit() or not position[1].isdigit() or position[2] not in ["N", "E", "S", "W"]:
#                 print("Invalid rover position format")
#                 continue

#             x, y = int(position[0]), int(position[1])
#             if x < 0 or x > plateau[0] or y < 0 or y > plateau[1]:
#                 print(f"Invalid initial position: ({x}, {y})")
#                 continue

#             instructions = input().strip()
#             if not all(c in "LRM" for c in instructions):
#                 print("Invalid instructions")
#                 continue

#             try:
#                 final_x, final_y, final_dir = move(plateau, (x, y, position[2]), instructions)
#                 print(f"{final_x} {final_y} {final_dir}")
#             except ValueError as e:
#                 print(str(e))

#         except EOFError:
#             break

# if __name__ == "__main__":
#     process_rovers()






# def move(plateau, rover_position, instructions):
#     directions = ["N", "E", "S", "W"]
#     x, y, direction = rover_position

#     for instruction in instructions:
#         if instruction == "L":
#             direction = directions[(directions.index(direction) - 1 + 4) % 4]
#         elif instruction == "R":
#             direction = directions[(directions.index(direction) + 1) % 4]
#         elif instruction == "M":
#             next_x, next_y = x, y

#             if direction == "N":
#                 next_y += 1
#             elif direction == "E":
#                 next_x += 1
#             elif direction == "S":
#                 next_y -= 1
#             elif direction == "W":
#                 next_x -= 1

#             if next_x < 0 or next_x > plateau[0] or next_y < 0 or next_y > plateau[1]:
#                 raise ValueError(f"Rover moved out of plateau bounds: ({next_x}, {next_y})")

#             x, y = next_x, next_y

#     return x, y, direction

# def process_rovers():
#     print("Give input:")
#     try:
#         plateau = tuple(map(int, input().split()))
#         if len(plateau) != 2 or any(n < 0 for n in plateau):
#             raise ValueError("Invalid plateau dimensions")
#     except ValueError:
#         print("\nResults:\nInvalid plateau dimensions")
#         return

#     results = []
    
#     while True:
#         try:
#             position_input = input().strip()
#             if not position_input:
#                 break

#             instructions = input().strip()
            
#             # Validate position format
#             position = position_input.split()
#             if len(position) != 3 or not position[0].isdigit() or not position[1].isdigit() or position[2] not in ["N", "E", "S", "W"]:
#                 results.append("Invalid rover position format")
#                 continue
                
#             # Validate coordinates
#             x, y = int(position[0]), int(position[1])
#             if x < 0 or x > plateau[0] or y < 0 or y > plateau[1]:
#                 results.append(f"Invalid initial position: ({x}, {y})")
#                 continue
                
#             # Validate instructions
#             if not all(c in "LRM" for c in instructions):
#                 results.append("Invalid instructions")
#                 continue

#             try:
#                 final_position = move(plateau, (x, y, position[2]), instructions)
#                 results.append(f"{final_position[0]} {final_position[1]} {final_position[2]}")
#             except ValueError as e:
#                 results.append(str(e))

#         except EOFError:
#             break

#     print("\nResults:")
#     for result in results:
#         print(result)

# if __name__ == "__main__":
#     process_rovers()







def move(plateau, rover_position, instructions):
    directions = ["N", "E", "S", "W"]
    x, y, direction = rover_position

    for instruction in instructions:
        if instruction == "L":
            direction = directions[(directions.index(direction) - 1 + 4) % 4]
        elif instruction == "R":
            direction = directions[(directions.index(direction) + 1) % 4]
        elif instruction == "M":
            next_x, next_y = x, y

            if direction == "N":
                next_y += 1
            elif direction == "E":
                next_x += 1
            elif direction == "S":
                next_y -= 1
            elif direction == "W":
                next_x -= 1

            if next_x < 0 or next_x > plateau[0] or next_y < 0 or next_y > plateau[1]:
                raise ValueError(f"Rover moved out of plateau bounds: ({next_x}, {next_y})")

            x, y = next_x, next_y

    return x, y, direction

def process_rovers():
    print("Give input:")
    try:
        plateau = tuple(map(int, input().split()))
        if len(plateau) != 2 or any(n < 0 for n in plateau):
            raise ValueError("Invalid plateau dimensions")
    except ValueError:
        print("\nResults:\nInvalid plateau dimensions")
        return

    results = []
    
    while True:
        try:
            position_input = input().strip()
            if not position_input:
                break

            instructions = input().strip()

            # Check if instructions are provided
            if not instructions:
                results.append("Invalid instructions")
                continue
            
            # Validate position format
            position = position_input.split()
            if len(position) != 3 or not position[0].isdigit() or not position[1].isdigit() or position[2] not in ["N", "E", "S", "W"]:
                results.append("Invalid rover position format")
                continue
                
            # Validate coordinates
            x, y = int(position[0]), int(position[1])
            if x < 0 or x > plateau[0] or y < 0 or y > plateau[1]:
                results.append(f"Invalid initial position: ({x}, {y})")
                continue
                
            # Validate instructions
            if not all(c in "LRM" for c in instructions):
                results.append("Invalid instructions")
                continue

            try:
                final_position = move(plateau, (x, y, position[2]), instructions)
                results.append(f"{final_position[0]} {final_position[1]} {final_position[2]}")
            except ValueError as e:
                results.append(str(e))

        except EOFError:
            break

    print("\nResults:")
    for result in results:
        print(result)

if __name__ == "__main__":
    process_rovers()
