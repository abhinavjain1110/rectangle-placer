import random
import matplotlib.pyplot as plt
import matplotlib.patches as patches

canvas_width, canvas_height = 100, 100

class RectanglePlacer:
    def __init__(self):
        self.rectangles = []

    def generate_random_rectangles(self, num_rectangles):
        return [(random.randint(10, 30), random.randint(10, 30)) for _ in range(num_rectangles)]

    def place_rectangles(self, space, rectangles):
        if not rectangles:
            return True  
        
        if space is None:
            return False  

        rect = rectangles[0]  
        width, height = rect

        if self.can_place_rectangle(space, width, height):
            new_space1, new_space2 = self.split_space(space, width, height)
            self.rectangles.append((space[0], space[1], width, height))  
            if self.place_rectangles(new_space1, rectangles[1:]) or self.place_rectangles(new_space2, rectangles[1:]):
                return True
            self.rectangles.pop()  

        if self.can_place_rectangle(space, height, width):
            new_space1, new_space2 = self.split_space(space, height, width)
            self.rectangles.append((space[0], space[1], height, width))
            if self.place_rectangles(new_space1, rectangles[1:]) or self.place_rectangles(new_space2, rectangles[1:]):
                return True
            self.rectangles.pop()  

        return False

    def can_place_rectangle(self, space, width, height):
        x, y, space_width, space_height = space
        return space_width >= width + 1 and space_height >= height + 1  

    def split_space(self, space, width, height):
        x, y, space_width, space_height = space
        new_space1 = (x + width + 1, y, space_width - width - 1, height)  
        new_space2 = (x, y + height + 1, space_width, space_height - height - 1)
        return new_space1, new_space2

    def plot_rectangles(self):
        fig, ax = plt.subplots()
        ax.set_xlim(0, canvas_width)
        ax.set_ylim(0, canvas_height)

        for (x, y, width, height) in self.rectangles:
            rect = patches.Rectangle((x, y), width, height, edgecolor='black', facecolor='cyan', linewidth=1)
            ax.add_patch(rect)

        plt.gca().set_aspect('equal', adjustable='box')
        plt.show()

def main():
    placer = RectanglePlacer()
    rectangles = placer.generate_random_rectangles(5) 
    initial_space = (0, 0, canvas_width, canvas_height)

    if not placer.place_rectangles(initial_space, rectangles):
        raise ValueError("Placement not possible with the given constraints.")
    placer.plot_rectangles()

if __name__ == "__main__":
    main()
