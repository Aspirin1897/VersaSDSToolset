import control


class ClearCommands():
    def __init__(self, sub_parser):
        self.subp = sub_parser
        self.parser = self.setup_parser()

    def setup_parser(self):
        parser_clear = self.subp.add_parser(
            'clear',
            help='clear VersaSDS configuration'
        )
        subp_clear = parser_clear.add_subparsers(dest='subargs_clear')

        p_crm = subp_clear.add_parser('crm', help = 'clear crm cluster resource')
        p_crm.set_defaults(func=self.clear_crm)

        p_vg = subp_clear.add_parser('vg', help = 'clear vg')
        p_vg.set_defaults(func=self.clear_vg)

        p_corosync = subp_clear.add_parser('corosync', help = 'clear corosync')
        p_corosync.set_defaults(func=self.clear_corosync)


        p_re = subp_clear.add_parser('re', help = 'restart sallite')
        p_re.set_defaults(func=self.restart_linstor)

        # p_pacemaker = subp_install.add_parser('pacemaker', help = 'uninstall pacemaker')
        # p_pacemaker.set_defaults(func=self.uninstall_pacemaker)

        # p_targetcli = subp_install.add_parser('targetcli', help = 'uninstall targetcli')
        # p_targetcli.set_defaults(func=self.uninstall_targetcli)

        parser_clear.set_defaults(func=self.clear_all)

    @classmethod
    def clear_crm(self,args):
        sc = control.PacemakerConsole()
        print('清除crm集群的相关资源')
        sc.clear_crm_res()

    @classmethod
    def clear_vg(self,args):
        sc = control.LVMConsole()
        print('清除vg')
        sc.remove_vg()

    # @classmethod
    # def uninstall_pacemaker(self,args):
    #     sc = control.VersaSDSSoftConsole()
    #     print('卸载pacemaker相关软件')
    #     sc.uninstall_pacemaker()

    @classmethod
    def clear_corosync(self,args):
        sc = control.PacemakerConsole()
        print('恢复 corosync 配置文件')
        sc.recover_corosync_conf()

    @classmethod
    def restart_linstor(self,args):
        sc = control.LinstorConsole()
        print('重启linstor集群的controller和satellite')
        sc.restart_linstor()

    @classmethod
    def clear_all(self,args):
        print('*start*')
        self.clear_crm(args)
        self.clear_vg(args)
        self.clear_corosync(args)
        self.restart_linstor(args)
        print('*success*')