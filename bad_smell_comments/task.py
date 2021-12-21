class Unit:
    # ...
    def flying(self, field, x: int, y: int, direction, flying: bool, crawling: bool, unit_speed: int = 1):

        if flying and crawling:
            raise ValueError('Рожденный ползать летать не должен!')

        if flying:
            unit_speed *= 1.2
            if direction == 'UP':
                new_y = y + unit_speed
                new_x = x
            elif direction == 'DOWN':
                new_y = y - unit_speed
                new_x = x
            elif direction == 'LEFT':
                new_y = y
                new_x = x - unit_speed
            elif direction == 'RIGHT':
                new_y = y
                new_x = x + unit_speed
        if crawling:
            unit_speed *= 0.5
            if direction == 'UP':
                new_y = y + unit_speed
                new_x = x
            elif direction == 'DOWN':
                new_y = y - unit_speed
                new_x = x
            elif direction == 'LEFT':
                new_y = y
                new_x = x - unit_speed
            elif direction == 'RIGHT':
                new_y = y
                new_x = x + unit_speed

            field.set_unit(x=new_x, y=new_y, unit=self)

#     ...
