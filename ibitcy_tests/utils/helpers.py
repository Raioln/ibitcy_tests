def capabilities_for_browser_name(browser_name):
    lower_browser_name = browser_name.lower()
    if lower_browser_name == 'chrome':
        return {
            "browserName": "chrome",
            "version": "77.0"
        }
    elif lower_browser_name == 'firefox':
        return {
            "browserName": "firefox",
            "version": "69.0"
        }
    elif lower_browser_name == 'opera':
        return {
            "browserName": "opera",
            "version": "63.0"
        }
