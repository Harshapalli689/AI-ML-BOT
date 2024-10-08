from Speak import speak
import platform
def sysinfo():
    my_system = platform.uname()
    print(f"System: {my_system.system}")
    print(f"Node Name: {my_system.node}")
    print(f"Release: {my_system.release}")
    print(f"Version: {my_system.version}")
    print(f"Machine: {my_system.machine}")
    print(f"Processor: {my_system.processor}")
    speak(my_system.system)
    speak(my_system.node)
    speak(my_system.release)
    speak(my_system.version)
    speak(my_system.machine)
    speak(my_system.processor)
