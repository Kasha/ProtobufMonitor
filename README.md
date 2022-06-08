# ProtobufMonitor

Generic Protobuf Monitor

## Description
1. Load generated python Protobuf modules (any [x]_pb.py). 
2. Parses them into objects. 
3. Creates a compatible UI per Protobuf Message (Tab+Tilte+Attributes)
4. Listens to Publisher for arrived Protobuf Message per topic (topic = Protobum message class name)
5. Displays in a tab, arrived Protobuf message
6. Topic + Protobuff message can be subscribed to a specific Publisher or a global configured Publisher.
7. Callback to handle arrived Topic+Protobuf Message can be configured per Protobuf message
8. Protobuf messages and/or related attributes can be configured to be ignored or hidden

## Getting started
1. Clone Project from Terminal or PyCharm->Git->Clone:
   - https://github.com/Kasha/ProtobufMonitor.git
3. Creating Python Protobuf classes (from windows)
   - Copy proto files into ProtobufMonotor root folder
   - Run the following command from ProtobufMonotor root folder: (assuming Project was cloned unde c:\)
     - protoc -I=C:/ProtobufMonitor/ --python_out=C:/ProtobufMonitor/ C:/ProtobufMonitor/[proto file].proto
2. Open PyCharm, Go To File-Settings: Add Interpreter
3. From main.py click on top taskbar to install required Python packages
4. Run Main.py

## Advanced
The following can be configured:
1. Subscription to a specific Protobuf Message Publisher URL address
2. Set Protobuf Messages to ignore Loading/Parsing/Listen to/Display
3. Set a Protobuf call back when it arrived, to process message data
4. Choose a set of Protobuf Message -> Attributes to be displayed
5. Set write_csv = True to log in excel arrived Protobuf message
Communication\Defines\config.yaml 
____________________________________________________________________________________________________________________________
1. Example configuration which ignores, timestamp_pb2.py, GisData_pb2.py, DataStructure_pb2.py, RailwayAI_pb2.py
2. Example of attributes to display for PositionData message, defined in GPSData python Protobuff modules
{GpsData_pb2: {PositionData: { gpsTime: 1, longitude: 1,latitude: 1, altitude: 1, heading: 1, yaw: 1, pitch: 1, roll: 1, velocity: 1, messageTime: 1, messageIndex: 1} }}}
3. Example of hidden PositionData Message attributes (or which to display):
Settings: messages_attr: {GpsData_pb2: {PositionData: { gpsTime: 1, longitude: 1, velocity: 1, messageTime: 1, messageIndex: 1} }}
4. Exmple of global Publisher address : server:{ip: 127.0.0.1, port: 12344)
_____________________________________________________________________________________________________________________________
messages: {mudules_preset: [{dir: .,filter_modules: [timestamp_pb2.py, GisData_pb2.py, DataStructure_pb2.py, RailwayAI_pb2.py], server:{ip: 127.0.0.1, port: 12344, write_csv: True, csv_frequency_sec: 0, callback: Protobuf1Callback}, filter_messages:{RadarICD_pb2: {GisPoiData: 1, GisPointsOfInterest: 1, GisSegments: 1, IMUReport: 1, RadarPresetRequest: 1, RadarPresetResponse: 1, RadarGpsData: 1, RadarMessageHeader: 1, RadarInit: 1, SetROI: 1}}, messages_server: {GpsData_pb2: {module_server:{ip: 127.0.0.1, port: 12344, write_csv: True, csv_frequency_sec: 0,callback: GpsData_pb2Callback}, message_server: {PositionData: { ip: 127.0.0.1, port: 12344, write_csv: True, csv_frequency_sec: 0, callback: PositionDataCallback}}}}, messages_attr: {GpsData_pb2: {PositionData: { gpsTime: 1, longitude: 1,latitude: 1, altitude: 1, heading: 1, yaw: 1, pitch: 1, roll: 1, velocity: 1, messageTime: 1, messageIndex: 1} }}}]}



