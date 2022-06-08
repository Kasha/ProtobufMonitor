from Communication.Managers.ModuleUI import TModuleUIForm
from Communication.Managers.ModuleManager import ModuleManager

if __name__ == '__main__':
 
    try:
        oModulesManager = ModuleManager()
        oModulesManager.start()
        oTModuleUIForm = TModuleUIForm() # When user choose to exit App, oModulesManager.stop() will do clean exit (close threads)
        oModulesManager.stop()
    except KeyboardInterrupt:
        oModulesManager.handle_cleanup(1) # Catch CTRL + C