<?php
namespace NethServer\Module;

/*
 * Copyright (C) 2011 Nethesis S.r.l.
 * 
 * This script is part of NethServer.
 * 
 * NethServer is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 * 
 * NethServer is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with NethServer.  If not, see <http://www.gnu.org/licenses/>.
 */

use Nethgui\System\PlatformInterface as Validate;

/**
 * Control ssh access to the system
 * 
 * @author Davide Principi <davide.principi@nethesis.it>
 */
class Ssh extends \Nethgui\Controller\AbstractController
{

    protected function initializeAttributes(\Nethgui\Module\ModuleAttributesInterface $base)
    {
        return \Nethgui\Module\SimpleModuleAttributesProvider::extendModuleAttributes($base, 'Security', 6);
    }

    public function initialize()
    {
        parent::initialize();
        $this->declareParameter('passwordAuth', Validate::BOOLEAN, array('configuration', 'sshd', 'PasswordAuthentication'));
        $this->declareParameter('rootLogin', Validate::BOOLEAN, array('configuration', 'sshd', 'PermitRootLogin'));
        $this->declareParameter('port', Validate::PORTNUMBER, array('configuration', 'sshd', 'TCPPort'));
        $this->declareParameter('status', Validate::SERVICESTATUS, array('configuration', 'sshd', 'status'));
        $this->declareParameter('access', $this->createValidator()->memberOf('private','public'), array('configuration', 'sshd', 'access'));
    }

    protected function onParametersSaved($changedParameters)
    {
        parent::onParametersSaved($changedParameters);
        $this->getPlatform()->signalEvent('nethserver-openssh-save');
    }

}
