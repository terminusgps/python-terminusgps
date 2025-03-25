import asyncio
from typing import Any

import twilio.rest
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from twilio.http.async_http_client import AsyncTwilioHttpClient

if not hasattr(settings, "TWILIO_SID"):
    raise ImproperlyConfigured("'TWILIO_SID' setting is required.")
if not hasattr(settings, "TWILIO_TOKEN"):
    raise ImproperlyConfigured("'TWILIO_TOKEN' setting is required.")
if not hasattr(settings, "TWILIO_FROM_NUMBER"):
    raise ImproperlyConfigured("'TWILIO_FROM_NUMBER' setting is required.")
if not hasattr(settings, "TWILIO_MESSAGING_SID"):
    raise ImproperlyConfigured("'TWILIO_MESSAGING_SID' setting is required.")


class TwilioCaller:
    def __init__(self) -> None:
        """Sets Twilio messaging session variables."""
        self.client_sid = settings.TWILIO_SID
        self.client_token = settings.TWILIO_TOKEN
        self.from_number = settings.TWILIO_FROM_NUMBER
        self.messaging_sid = settings.TWILIO_MESSAGING_SID

    def __enter__(self) -> "TwilioCaller":
        """Creates an asyncronous Twilio client."""
        self.client = twilio.rest.Client(
            self.client_sid, self.client_token, http_client=AsyncTwilioHttpClient()
        )
        return self

    def __exit__(self, exc_type, exc_value, exc_tb) -> None:
        return None

    async def create_notification(
        self, to_number: str, message: str, method: str = "sms"
    ) -> asyncio.Task[Any]:
        """
        Returns an awaitable notification task.

        Available methods are ``"sms"``, ``"call"`` and ``"phone"``.

        :param to_number: A phone number to notify.
        :type to_number: :py:obj:`str`
        :param message: A notification message.
        :type message: :py:obj:`str`
        :param method: A notification method. Default is ``"sms"``.
        :type method: :py:obj:`str`
        :returns: An awaitable task.
        :rtype: :py:obj:`~asyncio.Task`

        """
        match method:
            case "sms":
                return asyncio.create_task(
                    self.create_sms(to_number=to_number, message=message)
                )
            case "call" | "phone":
                return asyncio.create_task(
                    self.create_call(to_number=to_number, message=message)
                )
            case _:
                raise ValueError(f"Unsupported TwilioCaller method '{method}'.")

    async def create_call(self, to_number: str, message: str) -> None:
        """
        Calls ``to_number`` and reads ``message`` aloud.

        :param to_number: A phone number.
        :type to_number: :py:obj:`str`
        :param message: A message to be read aloud.
        :type message: :py:obj:`str`
        :returns: Nothing.
        :rtype: :py:obj:`None`

        """
        await self.client.calls.create_async(
            to=to_number,
            from_=self.from_number,
            twiml=f"<Response><Say>{message}</Say></Response>",
        )

    async def create_sms(self, to_number: str, message: str) -> None:
        """
        Texts ``message`` to ``to_number``.

        :param to_number: A phone number.
        :type to_number: :py:obj:`str`
        :param message: A message to be texted.
        :type message: :py:obj:`str`
        :returns: Nothing.
        :rtype: :py:obj:`None`

        """
        await self.client.messages.create_async(
            to=to_number,
            from_=self.from_number,
            body=message,
            messaging_service_sid=self.messaging_sid,
        )
