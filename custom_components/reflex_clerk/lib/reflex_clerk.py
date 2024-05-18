import reflex as rx

from .clerk_provider import clerk_provider
from .sign_in import sign_in
from .sign_up import sign_up


def install_signin_page(app: rx.App, publishable_key=None, route="/signin", **props) -> None:
    """
    This method installs a login page on the given App instance.
    It creates a centered layout using the rx.center() function,
    with a sign-in form generated by the [reflex_clerk.sign_in][] function.
    The sign-in form is vertically stacked using the rx.vstack() function,
    with a spacing of 7 units between each element. The entire layout is
    set to a height of 100vh.

    The login page is then installed on the App instance using the
    clerk_provider() function. If a publishable key is provided,
    it will be used for authentication.

    Example:
        ```python
        import reflex_clerk
        app = App()
        reflex_clerk.install_signin_page(app, publishable_key='your_publishable_key')
        ```

    Parameters:
        app (rx.App): The app instance to install the login page on.
        publishable_key (str): The publishable key to use for authentication.
        route (str): The route to install the login page on.  Defaults to "/signin".


    """

    assert route.startswith("/"), "Expected route to be absolute (e.g. starts with '/')"

    signin_page = clerk_provider(
        rx.center(
            rx.vstack(
                sign_in(
                    path=route,
                    **props
                ),
                align="center",
                spacing="7",
            ),
            height="100vh",
        ),
        publishable_key=publishable_key
    )

    app.pages[route[1:] + "/[[...signin]]/index"] = signin_page


def install_signup_page(app: rx.App, publishable_key=None, route="/signup", **props) -> None:
    """
    This method installs a signup page on the given App instance.
    It creates a centered layout using the rx.center() function,
    with a sign-in form generated by the [reflex_clerk.sign_up][] function.
    The sign-in form is vertically stacked using the rx.vstack() function,
    with a spacing of 7 units between each element. The entire layout is
    set to a height of 100vh.

    The login page is then installed on the App instance using the
    clerk_provider() function. If a publishable key is provided,
    it will be used for authentication.

    Example:
        ```python
        import reflex_clerk
        app = App()
        reflex_clerk.install_signup_page(app, publishable_key='your_publishable_key')
        ```

    Parameters:
        app (rx.App): The app instance to install the login page on.
        publishable_key (str): The publishable key to use for authentication.
        route (str): The route to install the login page on.  Defaults to "/signup".


    """

    assert route.startswith("/"), "Expected route to be absolute (e.g. starts with '/')"

    signup_page = clerk_provider(
        rx.center(
            rx.vstack(
                sign_up(
                    path=route,
                    **props
                ),
                align="center",
                spacing="7",
            ),
            height="100vh",
        ),
        publishable_key=publishable_key
    )

    app.pages[route[1:] + "/[[...signup]]/index"] = signup_page


def install_pages(
        app: rx.App,
        publishable_key=None,
        signin_route="/signin",
        signup_route="/signup",
        **props
) -> None:
    """Installs the signin and signup pages for the given app.

    Args:
        app (rx.App): The app instance for which the pages need to be installed.
        publishable_key (str, optional): The publishable key to be used for payment processing. Defaults to None.
        signin_route (str, optional): The route at which the signin page should be installed. Defaults to "/signin".
        signup_route (str, optional): The route at which the signup page should be installed. Defaults to "/signup".

    Example:
        ```python
        import reflex_clerk as clerk
        import reflex as rx
        app = rx.App()
        clerk.install_pages(app, publishable_key='your_publishable_key')
        ```

    Returns:
        None
    """
    install_signin_page(app, publishable_key=publishable_key, route=signin_route, **props)
    install_signup_page(app, publishable_key=publishable_key, route=signup_route, **props)
