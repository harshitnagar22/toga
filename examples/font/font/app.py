import toga
from toga.constants import BOLD, COLUMN, ITALIC, MONOSPACE, NORMAL, ROW


class FontApp(toga.App):
    def startup(self):
        # Load our own font files
        toga.Font.register("Endor", "resources/ENDOR___.ttf")
        toga.Font.register("Roboto", "resources/Roboto-Bold.ttf", weight=BOLD)
        toga.Font.register("Roboto", "resources/Roboto-Italic.ttf", style=ITALIC)
        toga.Font.register(
            "Roboto", "resources/Roboto-BoldItalic.ttf", weight=BOLD, style=ITALIC
        )
        toga.Font.register("Recursive", "resources/Recursive-VF.ttf")
        toga.Font.register("Recursive", "resources/Recursive-VF.ttf", weight=BOLD)
        toga.Font.register("Recursive", "resources/Recursive-VF.ttf", style=ITALIC)
        toga.Font.register(
            "Recursive", "resources/Recursive-VF.ttf", weight=BOLD, style=ITALIC
        )

        button_style = {
            "font_family": "awesome-free-solid",
            "font_size": 14,
        }

        main_box = toga.Box(style={"flex_direction": COLUMN})

        lbl1 = toga.Label("Endor", font_family="Endor", font_size=14)
        lbl2 = toga.Label("Endor bold", font_family="Endor", font_size=14, font_weight=BOLD)
        lbl3 = toga.Label(
            "Endor italic", font_family="Endor", font_size=14, font_style=ITALIC
        )
        lbl4 = toga.Label(
            "Endor bold italic",
            font_family="Endor",
            font_size=14,
            font_weight=BOLD,
            font_style=ITALIC,
        )
        lbl5 = toga.Label("Roboto", font_family="Roboto", font_size=14)
        lbl6 = toga.Label(
            "Roboto bold", font_family="Roboto", font_size=14, font_weight=BOLD
        )
        lbl7 = toga.Label(
            "Roboto italic", font_family="Roboto", font_size=14, font_style=ITALIC
        )
        lbl8 = toga.Label(
            "Roboto bold italic",
            font_family="Roboto",
            font_size=14,
            font_weight=BOLD,
            font_style=ITALIC,
        )
        lbl_r1 = toga.Label(
            "Recursive",
            font_family="Recursive",
            font_size=14,
        )
        lbl_r2 = toga.Label(
            "Recursive bold",
            font_family="Recursive",
            font_size=14,
            font_weight=BOLD,
        )
        lbl_r3 = toga.Label(
            "Recursive italic",
            font_family="Recursive",
            font_size=14,
            font_style=ITALIC,
        )
        lbl_r4 = toga.Label(
            "Recursive bold italic",
            font_family="Recursive",
            font_size=14,
            font_weight=BOLD,
            font_style=ITALIC,
        )

        unknown_style = {"font_family": "Unknown", "font_size": 14}
        lbl_u = toga.Label("Unknown", **unknown_style)
        lbl_ub = toga.Label(
            "Unknown bold",
            **unknown_style,
            font_weight=BOLD,
        )
        lbl_ui = toga.Label(
            "Unknown italic",
            **unknown_style,
            font_style=ITALIC,
        )
        lbl_ubi = toga.Label(
            "Unknown bold italic",
            **unknown_style,
            font_weight=BOLD,
            font_style=ITALIC,
        )

        main_box.add(
            lbl1,
            lbl2,
            lbl3,
            lbl4,
            lbl5,
            lbl6,
            lbl7,
            lbl8,
            lbl_r1,
            lbl_r2,
            lbl_r3,
            lbl_r4,
            lbl_u,
            lbl_ub,
            lbl_ui,
            lbl_ubi,
        )

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = toga.ScrollContainer(content=main_box)
        self.main_window.show()


if __name__ == "__main__":
    main().main_loop()
