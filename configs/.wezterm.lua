local wezterm = require("wezterm")

return {
    default_prog = {
        "powershell.exe",
        "-NoLogo",
    },

    default_cwd = "D:\\",

    initial_cols = 200,
    initial_rows = 50,

    font_size = 11.0,

    mouse_bindings = {
        {
            event = {
                Up = {
                    streak = 1,
                    button = "Right",
                },
            },
            mods = "NONE",
            action = wezterm.action_callback(function(window, pane)
                local selection = window:get_selection_text_for_pane(pane)

                if selection ~= "" then
                    -- 有选中文本:
                    -- 复制
                    window:perform_action(
                        wezterm.action.CopyTo("Clipboard"),
                        pane
                    )

                    -- 清除选择
                    window:perform_action(
                        wezterm.action.ClearSelection,
                        pane
                    )
                else
                    -- 无选中文本:
                    -- 粘贴
                    window:perform_action(
                        wezterm.action.PasteFrom("Clipboard"),
                        pane
                    )
                end
            end),
        },
    },
}