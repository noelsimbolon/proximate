import random
from timeit import default_timer as timer

import customtkinter
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import brute_force as bf
import divide_and_conquer as dnc
import util

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")


class App(customtkinter.CTk):
    # initialize inputs
    number_of_dimensions = 0
    number_of_points = 0
    points = None

    # Output variables for divide-and-conquer
    # ed_operations means the number of euclidean distance operations performed
    dnc_ed_operations = ""
    dnc_execution_time = ""
    dnc_closest_pair = None
    dnc_distance = None

    # Output variables for brute-force
    bf_ed_operations = ""
    bf_execution_time = ""
    bf_closest_pair = None
    bf_distance = None

    def __init__(self):
        super().__init__()

        # Font variables
        title_font = customtkinter.CTkFont(family="Arial Bold", size=-18)
        input_heading_font = customtkinter.CTkFont(family="Arial", size=-14)
        output_heading_font = customtkinter.CTkFont(family="Arial Bold", size=-14)
        placeholder_font = customtkinter.CTkFont(family="Arial", size=-12)
        select_theme_font = customtkinter.CTkFont(family="Arial", size=-12)
        randomize_input_font = customtkinter.CTkFont(family="Arial Bold", size=-12)
        start_button_font = customtkinter.CTkFont(family="Arial Bold", size=-12)
        status_font = customtkinter.CTkFont(family="Arial", size=-12)
        validation_label_font = customtkinter.CTkFont(family="Arial", size=-12)
        output_font = customtkinter.CTkFont(family="Arial", size=-14)

        # Main window configurations
        self.title("Closest Pair of Points")

        # ============ create two frames ============

        # configure grid layout (1 x 2)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.left_frame = customtkinter.CTkFrame(master=self, width=180)
        self.left_frame.grid(row=0, column=0, sticky="nswe", padx=(20, 0), pady=20)

        self.right_frame = customtkinter.CTkFrame(master=self)
        self.right_frame.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        # ============ left_frame ============

        # Configure grid layout (19 x 1)
        self.left_frame.grid_rowconfigure(0, minsize=10)  # empty row with minsize as spacing
        self.left_frame.grid_rowconfigure(2, minsize=20)  # space between input fields and app title
        self.left_frame.grid_rowconfigure(12, weight=1)  # empty row as spacing
        self.left_frame.grid_rowconfigure(15, minsize=20)  # empty row as spacing
        self.left_frame.grid_rowconfigure(18, minsize=20)  # empty row with minsize as spacing

        # App title
        self.app_title = customtkinter.CTkLabel(master=self.left_frame,
                                                text="Closest Pair of Points",
                                                font=title_font)
        self.app_title.grid(row=1, column=0, pady=10, padx=20)

        # Number of points
        self.number_of_points_label = customtkinter.CTkLabel(master=self.left_frame,
                                                             text="Number of Points:",
                                                             font=input_heading_font)
        self.number_of_points_label.grid(row=3, column=0, pady=0, padx=20)

        self.number_of_points_entry = customtkinter.CTkEntry(master=self.left_frame,
                                                             placeholder_text="Integer greater than 1",
                                                             font=placeholder_font)
        self.number_of_points_entry.grid(row=4, column=0, pady=5, padx=20, sticky="ew")

        self.number_of_points_validation_label = customtkinter.CTkLabel(master=self.left_frame,
                                                                        text="",
                                                                        text_color="red",
                                                                        font=validation_label_font)
        self.number_of_points_validation_label.grid(row=5, column=0, pady=(0, 10), padx=20)

        # Number of dimensions
        self.number_of_dimensions_label = customtkinter.CTkLabel(master=self.left_frame,
                                                                 text="Number of Dimensions:",
                                                                 font=input_heading_font)
        self.number_of_dimensions_label.grid(row=6, column=0, pady=0, padx=20)

        self.number_of_dimensions_entry = customtkinter.CTkEntry(master=self.left_frame,
                                                                 placeholder_text="Integer greater than 0",
                                                                 font=placeholder_font)
        self.number_of_dimensions_entry.grid(row=7, column=0, pady=5, padx=20, sticky="ew")

        self.number_of_dimensions_validation_label = customtkinter.CTkLabel(master=self.left_frame,
                                                                            text="",
                                                                            text_color="red",
                                                                            font=validation_label_font)
        self.number_of_dimensions_validation_label.grid(row=8, column=0, pady=(0, 10), padx=20)

        # Randomize input button
        self.randomize_input_button = customtkinter.CTkButton(master=self.left_frame,
                                                              text="Randomize Input",
                                                              font=randomize_input_font,
                                                              command=self.randomize_input)
        self.randomize_input_button.grid(row=9, column=0, pady=5, padx=20)

        # Start button
        self.start_button = customtkinter.CTkButton(master=self.left_frame,
                                                    text="Start",
                                                    font=start_button_font,
                                                    command=self.start)
        self.start_button.grid(row=10, column=0, pady=5, padx=20)

        self.space_label = customtkinter.CTkLabel(master=self.left_frame,
                                                  text="")
        self.space_label.grid(row=11, column=0, pady=5, padx=20)

        # Result
        self.status_heading_label = customtkinter.CTkLabel(master=self.left_frame,
                                                           text="Status:",
                                                           font=output_heading_font)
        self.status_heading_label.grid(row=13, column=0, pady=0, padx=20)

        # Prints the status of the program
        self.status_label = customtkinter.CTkLabel(master=self.left_frame,
                                                   text="",
                                                   font=status_font)
        self.status_label.grid(row=14, column=0, pady=0, padx=20)

        # Select GUI theme
        self.theme_label = customtkinter.CTkLabel(master=self.left_frame,
                                                  text="Select theme:",
                                                  font=select_theme_font)
        self.theme_label.grid(row=16, column=0, pady=0, padx=20, sticky="s")

        self.theme_options = customtkinter.CTkOptionMenu(master=self.left_frame,
                                                         values=["Dark", "Light", "System"],
                                                         font=select_theme_font,
                                                         command=change_appearance_mode)
        self.theme_options.grid(row=17, column=0, pady=5, padx=20, sticky="")

        # ============ right_frame ============

        # Configure grid layout (3x3) and its weights
        # weight=0 means it will not expand
        self.right_frame.rowconfigure((0, 1, 2, 3), weight=1)
        self.right_frame.columnconfigure((0, 1, 2), weight=1)
        self.right_frame.rowconfigure(1, weight=0)
        self.right_frame.columnconfigure(1, weight=0)
        self.right_frame.rowconfigure(3, weight=0)

        # Frame containing matplotlib 3D scatter plot (only shows up if the number of dimensions is 3)
        self.visualization_frame = customtkinter.CTkFrame(master=self.right_frame, fg_color="transparent")
        self.visualization_frame.grid(row=1, column=1, pady=(20, 20), padx=(20, 20), sticky="nswe")

        # Initialize a canvas for 3D scatter plot
        # This initialization is useful to avoid displaying multiple plots
        # by destroying the canvas before creating a new one every time a plot is want to be drawn
        self.visualization_canvas = FigureCanvasTkAgg(None, master=self.visualization_frame)

        # Initialize label for output when number of dimensions != 3
        self.points_output_label = customtkinter.CTkLabel(master=self.visualization_frame)

        # Output frame: contains output comparison between divide-and-conquer and brute-force
        self.output_frame = customtkinter.CTkFrame(master=self.right_frame)
        self.output_frame.grid(row=3, column=1, pady=(0, 20), padx=(20, 20), sticky="nswe")
        self.output_frame.rowconfigure((0, 1), weight=0)
        self.output_frame.columnconfigure((0, 1, 2, 3), weight=0)

        # output labels for divide-and-conquer algorithm
        self.divide_and_conquer_heading_label = customtkinter.CTkLabel(master=self.output_frame,
                                                                       text="Divide and Conquer",
                                                                       font=output_heading_font,
                                                                       anchor="n")
        self.divide_and_conquer_heading_label.grid(row=0, column=0, padx=(20, 10), pady=(20, 0))

        self.divide_and_conquer_label = customtkinter.CTkLabel(master=self.output_frame,
                                                               text="Euclidean Distance Operations: \n"
                                                                    "Execution Time: ",
                                                               font=output_font,
                                                               anchor="w",
                                                               justify="left")
        self.divide_and_conquer_label.grid(row=1, column=0, padx=(20, 10), pady=(0, 20))

        self.divide_and_conquer_output_label = customtkinter.CTkLabel(master=self.output_frame,
                                                                      text=f'{App.dnc_ed_operations}\n'
                                                                           f'{App.dnc_execution_time}',
                                                                      font=output_font,
                                                                      text_color="green",
                                                                      anchor="w",
                                                                      justify="left")
        self.divide_and_conquer_output_label.grid(row=1, column=1, padx=(0, 10), pady=(0, 20))

        # output labels for brute-force algorithm
        self.brute_force_heading_label = customtkinter.CTkLabel(master=self.output_frame,
                                                                text="Brute Force",
                                                                font=output_heading_font,
                                                                anchor="n")
        self.brute_force_heading_label.grid(row=0, column=2, padx=(20, 10), pady=(20, 0))

        self.brute_force_label = customtkinter.CTkLabel(master=self.output_frame,
                                                        text="Euclidean Distance Operations: \n"
                                                             "Execution Time: ",
                                                        font=output_font,
                                                        anchor="w",
                                                        justify="left")
        self.brute_force_label.grid(row=1, column=2, padx=(20, 10), pady=(0, 20))

        self.brute_force_output_label = customtkinter.CTkLabel(master=self.output_frame,
                                                               text=f'{App.bf_ed_operations}\n'
                                                                    f'{App.bf_execution_time}',
                                                               font=output_font,
                                                               text_color="green",
                                                               anchor="w",
                                                               justify="left")
        self.brute_force_output_label.grid(row=1, column=3, padx=(0, 10), pady=(0, 20))

    def randomize_input(self):
        """
        Randomizes input for the number of dimensions and the number of points
        """
        # Generate random integer
        App.number_of_dimensions = random.randint(1, 50)
        App.number_of_points = random.randint(2, 1000)

        # Clear entry first
        self.number_of_dimensions_entry.delete(0, 4)
        self.number_of_points_entry.delete(0, 4)

        # Then, insert the generated random integer
        self.number_of_dimensions_entry.insert(0, str(App.number_of_dimensions))
        self.number_of_points_entry.insert(0, str(App.number_of_points))

    def start(self):
        """
        Generate points and find the closest pair of points
        """
        # if the number of dimensions or the number of points is not valid,
        # display error message until it is valid
        if not (util.validate_number_of_dimensions(self.number_of_dimensions_entry.get()) and
                util.validate_number_of_points(self.number_of_points_entry.get())):

            # clear status label if input is invalid
            self.status_label.configure(text="")

            # if the number of dimensions is not valid
            if not util.validate_number_of_dimensions(self.number_of_dimensions_entry.get()):
                self.number_of_dimensions_validation_label.configure(text="Invalid number of dimensions.")
            else:
                self.number_of_dimensions_validation_label.configure(text="")

            # if the number of points is not valid
            if not util.validate_number_of_points(self.number_of_points_entry.get()):
                self.number_of_points_validation_label.configure(text="Invalid number of points.")
            else:
                self.number_of_points_validation_label.configure(text="")

            return

        # cool. if the input is valid, then clear any error message
        self.number_of_dimensions_validation_label.configure(text="")
        self.number_of_points_validation_label.configure(text="")

        # Assign inputs
        App.number_of_dimensions = int(self.number_of_dimensions_entry.get())
        App.number_of_points = int(self.number_of_points_entry.get())

        # Generate an array of arrays containing float
        App.points = np.random.uniform(low=-100, high=100, size=(App.number_of_points, App.number_of_dimensions))

        self.status_label.configure(text="Calculating...",
                                    text_color="yellow")

        dnc_start_time = timer()

        App.dnc_closest_pair, App.dnc_distance, App.dnc_ed_operations = \
            dnc.find_closest_pair_dnc(App.points, App.number_of_dimensions)

        dnc_end_time = timer()

        bf_start_time = timer()

        App.bf_closest_pair, App.bf_distance, App.bf_ed_operations = bf.find_closest_pair_bf(App.points)

        bf_end_time = timer()

        # If the number of dimensions is 3, display 3D scatter plot
        if App.number_of_dimensions == 3:
            self.visualize()
        else:
            # Destroy visualization canvas (if a plot is present this destroys it)
            self.visualization_canvas.get_tk_widget().destroy()
            # Destroy text output
            self.points_output_label.destroy()
            self.points_output_label = customtkinter.CTkLabel(master=self.visualization_frame,
                                                              text=f'Closest Pair of Points: '
                                                                   f'{App.dnc_closest_pair[0]} and '
                                                                   f'{App.dnc_closest_pair[1]}\n\n'
                                                                   f'Euclidean Distance: '
                                                                   f'{App.dnc_distance}',
                                                              justify="left")
            self.points_output_label.pack(padx=20, pady=20)

        self.status_label.configure(text="Done!",
                                    text_color="green")

        App.dnc_execution_time = f"{dnc_end_time - dnc_start_time:.5f} s"
        App.bf_execution_time = f"{bf_end_time - bf_start_time:.5f} s"

        self.show_ed_operations_and_execution_time()

    def visualize(self):
        """
        Draw a 3D scatter plot if the number of dimensions is 3
        """

        first_point = App.dnc_closest_pair[0]
        second_point = App.dnc_closest_pair[1]

        # initialize arrays containing coordinates of points for each axis
        x_coordinates = np.array([])
        y_coordinates = np.array([])
        z_coordinates = np.array([])

        for i in range(App.number_of_points):
            # if the current point is one of the points in the closest pair, don't append it
            if any(np.array_equal(App.points[i], p) for p in App.dnc_closest_pair):
                continue
            x_coordinates = np.append(x_coordinates, App.points[i][0])
            y_coordinates = np.append(y_coordinates, App.points[i][1])
            z_coordinates = np.append(z_coordinates, App.points[i][2])

        # Create the plot
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        # Scatter all points except the closest pair in blue
        ax.scatter(x_coordinates, y_coordinates, z_coordinates, alpha=0.1, c='b')

        # Scatter the closest pair of points in red
        ax.scatter([first_point[0], second_point[0]],
                   [first_point[1], second_point[1]],
                   [first_point[2], second_point[2]], c='r')

        # Draw a line between the closest pair of points
        ax.plot([first_point[0], second_point[0]],
                [first_point[1], second_point[1]],
                [first_point[2], second_point[2]], c='k')

        # Add labels and title
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.set_title('3D Scatter Plot with Highlighted Closest Pair of Points')

        # Add text annotations for closest pair of points and its distance
        fig.text(0.03, 0.03, f'Closest Pair of Points: '
                             f'({first_point[0]:.3f}, {first_point[1]:.3f}, {first_point[2]:.3f}) and '
                             f'({second_point[0]:.3f}, {second_point[1]:.3f}, {second_point[2]:.3f})\n'
                             f'Euclidean Distance: {App.dnc_distance:.3f}', fontsize=8, color='k')

        # Destroy visualization canvas (if a plot is present this destroys it)
        self.visualization_canvas.get_tk_widget().destroy()

        # Destroy text output
        if self.points_output_label.cget("text") != "CTkLabel" or "":
            self.points_output_label.pack_forget()

        # Then, draw a new plot to a Tkinter canvas
        self.visualization_canvas = FigureCanvasTkAgg(fig, master=self.visualization_frame)
        self.visualization_canvas.draw()
        self.visualization_canvas.get_tk_widget().pack()

    def show_ed_operations_and_execution_time(self):
        """
        Display Euclidean distance operations and execution time in the GUI
        """
        self.divide_and_conquer_output_label.configure(text=f'{App.dnc_ed_operations}\n'
                                                            f'{App.dnc_execution_time}')
        self.brute_force_output_label.configure(text=f'{App.bf_ed_operations}\n'
                                                     f'{App.bf_execution_time}')


def change_appearance_mode(new_appearance_mode: str):
    """
    Changes the GUI theme
    :param new_appearance_mode: string: "dark", "light", or "system"
    """
    customtkinter.set_appearance_mode(new_appearance_mode)


if __name__ == "__main__":
    app = App()
    app.mainloop()
