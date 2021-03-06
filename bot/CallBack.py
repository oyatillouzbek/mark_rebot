
class CallBack(object):
    def __init__(self, view, db):
        self.view = view
        self.db = db
        self.map_method = {
            'main'        : view.main,
            'help'        : view.help,
            'ch_add'      : view.ch_add,
            'ch_sett'     : view.ch_setting,
            'ch_list'     : view.ch_list,
            'set_mark'    : view.set_mark,
            'photo_mark'  : view.photo_mark,
            'bot_info'    : view.bot_info,
            'del_ch_sett' : view.del_ch_sett,   
            
            'mark_size'   : view.mark_size,
            'pos_mark'    : view.pos_mark,
            'font_style'  : view.font_style,
            'color_mark'  : view.color_mark,
            'margin_mark' : view.margin_mark,    
            'transparent_mark':view.transparent_mark,

            'instruct_desktop':view.instruct_desktop,
            'instruct_android':view.instruct_android,
        }


    def main(self, call):
        print(f'\nUser {call.from_user.first_name}, id:{call.from_user.id},\
         send data: {call.data}, username: {call.from_user.username}')
        user_id = call.from_user.id
        data = call.data.split('$')
        cmd = data[0].split()
        if len(data) == 2:
            
            args = dict([n.split('=') for n in data[1].split(', ')])

        else:
            args = {}

        if cmd[0] == 'set':
            if cmd[1] == 'ch':
                if cmd[2] == 'status':
                    self.db.switch_status(user_id)
                else:
                    
                    self.db.channel_set(user_id, cmd[2], cmd[3])
                self.view.ch_setting(user_id)

                    
        elif cmd[0] == 'open':
            
      #      try:
            if 'ch_id' in args:
                self.db.user_set(user_id, 'group_select', args['ch_id'])

                del args['ch_id']
            self.db.user_set(user_id, 'menu_select', cmd[1])
            self.map_method[cmd[1]](user_id, **args)
        #    except Exception as e:
                
        #        print('Error map method: ', e)
        #        print('CMD: ', cmd, ' ARGS: ', args)
        #        print(data)
        #        self.view.main(user_id)
            
            

        elif cmd[0] == 'del':
            if cmd[1] == 'ch_sett':
                self.db.del_ch_sett(user_id)
                self.view.ch_list(user_id)
        elif cmd[0] == 'add':
            if cmd[1] == 'ch_sett':
                
                self.db.new_channel(user_id, args['ch_id'], 'No-name')
                self.db.user_set(user_id, 'group_select', args['ch_id'])
                self.view.ch_setting(user_id,)

            
