from Communication.Managers.ModuleUI import TModuleUIForm
from Communication.Managers.ModuleManager import ModuleManager

"""
server_publisher.publish_msg(imu_report.SerializeToString(), topic=imu_report.DESCRIPTOR.name.encode())
server_publisher.publish_msg(status_report.SerializeToString(), topic=status_report.DESCRIPTOR.name.encode())
server_publisher.publish_msg(detection_report.SerializeToString(), topic=detection_report.DESCRIPTOR.name.encode())
server_publisher.publish_msg(engine.preset_response_msg.SerializeToString(),
                                         topic=engine.preset_response_msg.DESCRIPTOR.name.encode())
"""
if __name__ == '__main__':
 
    try:
        oModulesManager = ModuleManager()
        oModulesManager.start()
        oTModuleUIForm = TModuleUIForm()
        oModulesManager.stop()
    except KeyboardInterrupt:
        oModulesManager.handle_cleanup(1)