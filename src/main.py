import input_validation
import customtkinter
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from timeit import default_timer as timer


customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")


class App(customtkinter.CTk):
    execution_time = None

    def __init__(self):
        super().__init__()

        # Font variables
        title_font = customtkinter.CTkFont(family="Arial Bold", size=-18)
        input_heading_font = customtkinter.CTkFont(family="Arial", size=-14)
        output_heading_font = customtkinter.CTkFont(family="Arial Bold", size=-14)
        placeholder_font = customtkinter.CTkFont(family="Arial", size=-12)
        select_theme_font = customtkinter.CTkFont(family="Arial", size=-12)
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
        self.left_frame.grid_rowconfigure(10, weight=1)  # empty row as spacing
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
        self.number_of_points_label.grid(row=2, column=0, pady=0, padx=20)

        self.number_of_points_entry = customtkinter.CTkEntry(master=self.left_frame,
                                                             placeholder_text="Integer greater than 1",
                                                             font=placeholder_font)
        self.number_of_points_entry.grid(row=3, column=0, pady=5, padx=20, sticky="ew")

        self.number_of_points_validation_label = customtkinter.CTkLabel(master=self.left_frame,
                                                                        text="",
                                                                        text_color="red",
                                                                        font=validation_label_font)
        self.number_of_points_validation_label.grid(row=4, column=0, pady=(0, 10), padx=20)

        # Number of dimensions
        self.number_of_dimensions_label = customtkinter.CTkLabel(master=self.left_frame,
                                                                 text="Number of Dimensions:",
                                                                 font=input_heading_font)
        self.number_of_dimensions_label.grid(row=5, column=0, pady=0, padx=20)

        self.number_of_dimensions_entry = customtkinter.CTkEntry(master=self.left_frame,
                                                                 placeholder_text="Integer greater than 0",
                                                                 font=placeholder_font)
        self.number_of_dimensions_entry.grid(row=6, column=0, pady=5, padx=20, sticky="ew")

        self.number_of_dimensions_validation_label = customtkinter.CTkLabel(master=self.left_frame,
                                                                            text="",
                                                                            text_color="red",
                                                                            font=validation_label_font)
        self.number_of_dimensions_validation_label.grid(row=7, column=0, pady=(0, 10), padx=20)

        # Start button
        self.start_button = customtkinter.CTkButton(master=self.left_frame,
                                                    text="Start",
                                                    font=start_button_font,
                                                    command=self.start)

        self.start_button.grid(row=8, column=0, pady=5, padx=20)

        self.status_label = customtkinter.CTkLabel(master=self.left_frame,
                                                   text="",
                                                   font=status_font)
        self.status_label.grid(row=9, column=0, pady=5, padx=20)

        # Result
        self.result_label = customtkinter.CTkLabel(master=self.left_frame,
                                                   text="Result:",
                                                   font=output_heading_font)
        self.result_label.grid(row=11, column=0, pady=0, padx=20)

        # Prints the closest pair of points and their distance
        self.closest_pair_of_points_label = customtkinter.CTkLabel(master=self.left_frame,
                                                                   text="",
                                                                   text_color="green",
                                                                   font=output_font)
        self.closest_pair_of_points_label.grid(row=12, column=0, pady=0, padx=20)

        # Execution time
        self.exec_label = customtkinter.CTkLabel(master=self.left_frame,
                                                 text="Execution time:",
                                                 font=output_heading_font)
        self.exec_label.grid(row=13, column=0, pady=0, padx=20)

        self.execution_time_label = customtkinter.CTkLabel(master=self.left_frame,
                                                           text="",
                                                           text_color="green",
                                                           font=output_font)
        self.execution_time_label.grid(row=14, column=0, pady=0, padx=20)

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
        self.right_frame.rowconfigure((0, 1, 2), weight=1)
        self.right_frame.columnconfigure((0, 1, 2), weight=1)
        self.right_frame.rowconfigure(1, weight=0)
        self.right_frame.columnconfigure(1, weight=0)

        self.visualization_frame = customtkinter.CTkFrame(master=self.right_frame)
        self.visualization_frame.grid(row=1, column=1, pady=(20, 20), padx=(20, 20), sticky="nswe")

        # Create the plot
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter([1, 2, 3], [4, 5, 6], [7, 8, 9])

        # Add the plot to a Tkinter canvas
        canvas = FigureCanvasTkAgg(fig, master=self.visualization_frame)
        canvas.draw()
        canvas.get_tk_widget().pack()

    def set_execution_time(self):
        """
        Display execution time in the GUI
        """
        self.execution_time_label.configure(text=App.execution_time)

    def start(self):
        """
        Generate points and find the closest pair of points
        """
        # if the number of dimensions or the number of points is not valid,
        # display error message until it is valid
        if not (input_validation.validate_number_of_dimensions(self.number_of_dimensions_entry.get()) and
                input_validation.validate_number_of_points(self.number_of_points_entry.get())):

            # if the number of dimensions is not valid
            if not input_validation.validate_number_of_dimensions(self.number_of_dimensions_entry.get()):
                self.number_of_dimensions_validation_label.configure(text="Invalid number of dimensions.")
            else:
                self.number_of_dimensions_validation_label.configure(text="")

            # if the number of points is not valid
            if not input_validation.validate_number_of_points(self.number_of_points_entry.get()):
                self.number_of_points_validation_label.configure(text="Invalid number of points.")
            else:
                self.number_of_points_validation_label.configure(text="")

            return

        # cool. if the input is valid, then clear any error message
        self.number_of_dimensions_validation_label.configure(text="")
        self.number_of_points_validation_label.configure(text="")

        start_time = timer()

        # do divide and conquer

        end_time = timer()

        elapsed_time = end_time - start_time
        App.execution_time = f"{elapsed_time:.2f} s"


def change_appearance_mode(new_appearance_mode: str):
    """
    Changes the GUI theme
    :param new_appearance_mode: string: "dark", "light", or "system"
    """
    customtkinter.set_appearance_mode(new_appearance_mode)


if __name__ == "__main__":
    app = App()
    app.mainloop()
