from pbf.Commands.command_manager import CommandConfig, RegisterCommands

commands = [CommandConfig("add connection", "pbf_toggl.Commands.add_connection.AddConnection", description="Creates a connection for the given token in the Toggl Settings"),
            CommandConfig("add toggl-settings", "pbf_toggl.Commands.add_toggl_settings.AddTogglSettings", description="Add Toggl settings to the current project"),
            CommandConfig("new toggl-project", "pbf_toggl.Commands.new_toggl_project.NewTogglProject", description="Create a new Toggl Project"),
            CommandConfig("start timer", "pbf_toggl.Commands.start_timer.StartTimerCommand", description="Start the Toggl Timer"),
            CommandConfig("stop timer", "pbf_toggl.Commands.stop_timer.StopTimerCommand", description="Stop the current timer for Toggl")]

RegisterCommands(commands)