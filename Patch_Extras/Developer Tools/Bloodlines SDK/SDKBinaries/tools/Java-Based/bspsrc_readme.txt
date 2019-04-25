BSPSource
=========

BSPSource is a map decompiler for [Source engine](http://developer.valvesoftware.com/wiki/Source) maps, written in Java.
It decompiles .bsp map files back to .vmf files that can be loaded in Hammer, Valve's official level editor.

BSPSource is based on a reengineered version of [VMEX 0.98g](http://www.bagthorpe.org/bob/cofrdrbob/vmex.html) by Rof, which is no longer developed and lacks
support for newer Source engine games.

Downloads
---------

The latest version is available in the "release" tab. Older versons are available for download [here](http://ata4.info/downloads/apps/bspsource/).

Improvements and changes compared to VMEX 0.98g
-----------------------------------------------

* Support for more and newer Source engine games up to Dota 2.
* Support for new entity types:
	* [func_areaportal](http://developer.valvesoftware.com/wiki/func_areaportal)
	* [func_areaportalwindow](http://developer.valvesoftware.com/wiki/func_areaportalwindow)
	* [func_occluder](http://developer.valvesoftware.com/wiki/func_occluder)
	* [info_lighting](http://developer.valvesoftware.com/wiki/info_lighting)
* Support for the tools/blocklight texture.
* Support for compressed and big-endian encoded maps (XBox 360, PS3)
* Decompiles VMEX maps flagged with protection and at least detects other anti-decompiling methods.
* Improved support for [prop_static](http://developer.valvesoftware.com/wiki/prop_static) and [info_overlay](http://developer.valvesoftware.com/wiki/info_overlay)</a>.
* Improved console output.
* New graphical user interface with output window.
* New command line interface.
* New integrated pakfile extractor.
* Numerous bug fixes.
* Open source.

Limitations and known bugs
--------------------------

* Some internal entities that are entirely consumed by vbsp can't be restored. This includes following entities:
	* [func_instance](http://developer.valvesoftware.com/wiki/func_instance)
	* [func_instance_parms](http://developer.valvesoftware.com/wiki/func_instance_parms)
	* [func_instance_origin](http://developer.valvesoftware.com/wiki/func_instance_origin)
	* [func_viscluster](http://developer.valvesoftware.com/wiki/func_viscluster)
	* [info_no_dynamic_shadow](http://developer.valvesoftware.com/wiki/info_no_dynamic_shadow)
* Areaportal and occluder entities are somewhat difficult to decompile and sometimes have missing brushes or wrong textures.


-- Changelog --

(* Source-code related changes)
1.3-beta
- Reworked GUI and CLI
- Files from directories can now be added with drag-and-drop
- Added support for maps from the leaked HL2 beta
- Areaportals can now be decompiled with a flat brush if the original brush can't be found
- Occluders should now always be decompiled correctly. Exact brush dimensions may differ from the original VMF, though.
- Skipping displacements will now create flat brushes without displacement data instead of skipping the brushes entirely
- Overlays should now work in face decompiling modes
- Added additional VMF debug information
- Debug information written into the VMF now have keys prefixed with "bspsrc_"
- Moved BSP analysis and pakfile extraction to a separate tool collection which will be released later
- Fixed many bugs for face decompiling modes, results are now close to VMEX again
- Fixed an instance rotation error causing some brushes being flipped around on the y-axis
- Fixed toolsinvisible and toolsnodraw not always being detected correctly
* Tons of refactoring, especially in the classes Winding, FaceSource and BrushSource
* Merged DisplacementSource with FaceSource
* Added many comments found in the original VMEX source code and Source SDK

1.2.3
- Added support to select multiple files in GUI
- Improved entity reader, again
* Integrated LZMA library into bsplib
* Restructured bsplib to support file writing

1.2.2
- Fixed problems caused by missing model indices that occurred in one map
- Entity rotation correction is now enabled on default again, but is ignored for BSP versions below 21
- Further improved entity reader, fixing some possible bugs with inputs and outputs
- Added detection of Bloody Good Time maps
* Implemented Apache Commons IO for some file/stream operations

1.2.1
- Instance entities with fixup names are now automatically grouped to visgroups (prefix only)
- Fixed "Texture axis perpendicular to face" errors when using the rotation fix (hopefully)

1.2
- Added support to process all maps inside a directory (CLI only)
- Added correct handling for info_overlay_accessor entities
- Fixed possible game detection bugs
* Changed most remaining messages to use the internal Java logging system

1.2-beta2:
- Improved game detection and added some Source games
- Added missing option to turn off lump file loading in CLI
- Fixed issue with Portal 2 maps for PC
- Fixed pakfile extraction not updating the suggested destination path when changing the BSP file
* Changed all messages in bsplib to use the internal Java logging system

1.2-beta:
- Added initial support and detection for Portal 2 maps
- Added button to extract the pakfile without decompiling the map in the process
- Fixed bug that prevented info_overlay decompiling from being disabled by the user
- Fixed an uncaught exception caused by invalid vector strings
- The cameras in Hammer are now positioned above the spawn points (info_player_*)
- Re-enabled debug information for bsplib

1.1.1:
- Added experimental support for big-endian byte order and compressed BSP files (used for PS3/X360)
- Added lump alignment table to structure analysis
- Entity rotation correction is now disabled on default to avoid wrong rotations in older BSP versions
- Files with upper-case file extensions are now recognized correctly
- Fixed possible problems caused by NaN float values
* Changed package names

1.1
- Multiplayer Dark Messiah maps are now supported again
- Optimized analysis mode

1.1-beta3
- Fixed broken selection of face and back-face textures in CLI
- Fixed freeze when processing the embedded Zip file multiple times

1.1-beta2
- Fixed support for singleplayer Dark Messiah maps (multiplayer support is currently broken, though)
- Fixed exception error in the compile parameter analysis and debug mode
- Lowered requirements to Java 5

1.1-beta:
- Added new analysis mode: compile parameters
- Added manual analysis mode selection for GUI and CLI
- Added support for the toolsblock_los texture
- Re-added lost detection of entities with missing class name
- Face and back-face textures are no longer limited to presets and can be chosen as string in CLI mode
- Static props now have shared info_lighting entities
- Texture shifts are now normalized to the texture's width and height
- Fixed "Appearance" values for named lights
- Fixed fatal errors when encountering minor lump length/offset anomalies
- Fixed wrong (back-)face texture selection
- Fixed invalid texinfo indices when decompiling original faces for BSP v20 and above
* Converted most static integer fields to enumerations
* Optimized tool texture handling
* Entity key-values are now stored in maps again, except for the I/O

1.0.1:
- Fixed entity brush rotation using wrong rotation axes
- Added missing command line parameter for the entity brush rotation fix

1.0:
- Fixed bug that prevented external lump loading to be turned off
- Fixed exception when opening maps in the same directory as bspsrc.jar
- Fixed some bugs for Zeno Clash maps
- Fixed various other map loading bugs
- Fixed pakfile reading error caused by a bug in Java's Zip implementation
- Minor GUI improvements
- The decompile/analyze buttons will no longer stay disabled on fatal errors
- Added application icon, thanks SpAM_CAN!
- Added support to override automatic game detection with manual selection (command line only for now)
- Added more analysis information
* Moved BSPProtect decryption code to a separate tool
* Created external bsplib library that can be used by other applications

1.0-beta:
- GUI re-design for better usability
- Added option to skip entity and/or brush decompiling entirely
- Added detection for nodraw texture hack by IID_BSP
- Added support for external lump files (.lmp)
- Added support for entity decryption of maps protected with BSPProtect (command line only, requires a key to be passed via parameter -k or -bspprotkey)
- Added support for newer overlay properties (fadedist, cpulevel, gpulevel)
- Added "Analyze" button, which prints information about the currently selected BSP file
- info_ladder entities will now be removed during decompile
- Fixed "null" texture bug for decompiled faces
- Fixed bug that prevented info_cubemap entities to have any brush sides assigned
- Fixed brush entities sometimes having the wrong visible rotation in Hammer (may cause "texture axis perpendicular to face" errors)
- Improved text format for information mode
- Non-debug decompiling is now less verbose
- Changed most command line parameters
* Splitted BspSource class into smaller modules
* Moved some parts of BspReader into the new LumpReader class
* Added Javadoc for many methods and classes

0.99.2:
- Added support for "Dark Messiah of Might and Magic" and "Vampire: The Masquerade - Bloodlines"
- Added file drag & drop support for the GUI
- Missing entity class names will now be replaced with "unknown_entity" to prevent Hammer crashes (inspired by the mapfix tool for Bloodlines Revival)
- Enhanced game detection
- Fixed false entity obfuscation detection for simple maps

0.99.1:
- Added detection for entity encryption by BSPProtect
- Added detection for entity obfuscation by IID
- Added information output only mode for command line
- Some GUI improvements, such as custom VMF file selection
- Improved CLI interface

0.99:
- Renamed to BSPSource and using new versioning scheme
- Improved func_areaportal brush decompiling
- Added support for func_areaportalwindow brushes
- Added experimental support for func_occluder brushes (brush sides may have wrong textures)
- Added support for info_lighting entities
- Added support for toolsblocklight texture
- Improved readability of console output
- Reduced default decimal precision from 8 to 6 to lower rounding errors
- When a map contains decompiling protections, the used methods will be displayed
* Major code refactoring and optimization

0.98g_mod7:
- Fixed overlays sometimes having too many assigned faces
- Fixed missing entity I/O entries

0.98g_mod6:
- Fixed overlays with no assigned faces for non-displacement brushes
- Fixed missing func_detail brushes in Alien Swarm maps
- Added very basic support for func_areaportal brushes (no func_areaportalwindow yet, though)
* Improved entity reading code and lots of small cleanups

0.98g_mod5:
- Fixed wrong entity input/output handling for Alien Swarm
* Improved game detection code

0.98g_mod4:
- Added support for Alien Swarm, Zeno Clash and The Ship
- New prop_statics are now fully supported (dxlevel, cpulevel, gpulevel, disableX360)
* More code cleanup

0.98g_mod3:
- The decompiling protection warning will now be displayed for all protection methods
* Code cleanup

0.98g_mod2:
- Enhanced support for BSP version 21, especially for prop_static
- func_simpleladder entities are now converted to func_ladder
- Fixed some texture name bugs
- Areaportal brushes now have at least the correct texture

0.98g_mod1:
- Basic support for BSP version 21 (L4D2)
- Fixed a bug when decompiling L4D1 maps
- Fixed some other small bugs
- Lightweight vmf output by removing values that are regenerated by Hammer itself
- Decompiling will no longer be refused when processing protected maps. Instead, a kind warning message is displayed FYI.
- Cleared up console output
- New GUI rewritten from scratch with more settings and a console output window
