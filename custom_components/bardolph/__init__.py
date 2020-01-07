DOMAIN = 'bardolph'

SLASH = '/'

ATTR_FLS = 'files'
ATTR_DIR = 'dir'
ATTR_SCR = 'script'
DFLT_FLS = 'cycle-color.ls off-all.ls'
DFLT_DIR = '/config/custom_components/bardolph/scripts/'
DFLT_SCR = '' #'on all'

ATTR_TXT = 'txtfile'
DFLT_TXT = 'lscap.txt'
DFLT_TDR = '/share/bardolph/'
ATTR_OPT = 'options'
DFLT_OPT = '--text'

def setup(hass, config):

    def handle_lsrun(call):
        import re
        import sys
        from bardolph.controller import run
        from ast import literal_eval

        dict_lsrun = literal_eval(str(hass.states.get('bardolph.lsrun')).split('=')[1].split(' @')[0])

        files = call.data.get(ATTR_FLS, '').strip()
        folder = call.data.get(ATTR_DIR, '').replace(' ','')
        script = call.data.get(ATTR_SCR, '').strip()

        if files + folder + script == "":
            script = call.data.get(ATTR_SCR, dict_lsrun[ATTR_SCR]).strip()

        files = call.data.get(ATTR_FLS, dict_lsrun[ATTR_FLS]).strip()
        folder = call.data.get(ATTR_DIR, dict_lsrun[ATTR_DIR]).replace(' ','')

        if script != "":
            sys.argv = ['lsrun','-s',script]
            dict_lsrun[ATTR_SCR] = script
        else:
            if not folder.endswith('/'):
                folder = folder + '/'
            sys.argv = [folder+e for e in files.split()]
            sys.argv.insert(0, 'lsrun')

            dict_lsrun[ATTR_FLS] = files
            dict_lsrun[ATTR_DIR] = folder
            dict_lsrun[ATTR_SCR] = ""
        
        sys.argc = len(sys.argv)

        hass.states.set('bardolph.lsrun', dict_lsrun)

        try:
            run.main()
        finally:
            return

        # end handle_call for lsrun

    def handle_lscap(call):

        import re
        import sys
        from bardolph.controller import snapshot
        from ast import literal_eval

        dict_lscap = literal_eval(str(hass.states.get('bardolph.lscap')).split('=')[1].split(' @')[0])

        txt = call.data.get(ATTR_TXT, dict_lscap[ATTR_TXT]).replace(' ','')
        opt = call.data.get(ATTR_OPT, dict_lscap[ATTR_OPT]).strip()

        sys.argv = opt.split()
        sys.argv.insert(0, 'lscap')
        sys.argc = len(sys.argv)

        dict_lscap[ATTR_TXT] = txt
        dict_lscap[ATTR_OPT] = opt
        hass.states.set('bardolph.lscap', dict_lscap)

        import os
        if not os.path.exists(DFLT_TDR):
            os.mkdir(DFLT_TDR)

        txtpath = DFLT_TDR + ((SLASH + txt).split(SLASH)[-1])

        try:
            orig_stdout = sys.stdout
            #with open('/share/bardolph/lscap.txt', 'w') as f:
            with open(txtpath, 'w') as f:
                sys.stdout = f
                snapshot.main()
        finally:
            sys.stdout.close()
            sys.stdout=orig_stdout
            return

        # end handle_call for lscap

    hass.services.register(DOMAIN, 'lsrun', handle_lsrun)
    hass.states.set('bardolph.lsrun', {ATTR_FLS : DFLT_FLS, ATTR_DIR : DFLT_DIR, ATTR_SCR : DFLT_SCR})

    hass.services.register(DOMAIN, 'lscap', handle_lscap)
    hass.states.set('bardolph.lscap', {ATTR_TXT : DFLT_TXT, ATTR_OPT : DFLT_OPT})

    import sys
    sys.path.append('..')

    return True
    
# end Setup