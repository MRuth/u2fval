#    Copyright (C) 2014  Yubico AB
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
WSGI file for u2f-val.
To function, clients will need to be specified via the REMOTE_USER WSGI environ
key. This can be provided by the webserver (using HTTP auth, or hard-coded) or
by some middleware.
"""
from u2fval.config import settings
from u2fval.core.api import create_application

application = create_application(settings)
